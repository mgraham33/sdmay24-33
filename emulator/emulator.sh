#!/bin/bash

# Configure the emulator, update the C file, and run the emulator

# Replace 'user' with the current user's account name
USERNAME=$(whoami)

# Define the path to the PICO_SDK
PICO_SDK_PATH="/home/$USERNAME/sdmay24-33/emulator/pico-sdk"

# Check if the line already exists in ~/.bashrc
if ! grep -qxF "export PICO_SDK_PATH=$PICO_SDK_PATH" ~/.bashrc; then
    echo 'export PICO_SDK_PATH='"$PICO_SDK_PATH" | sudo tee -a ~/.bashrc > /dev/null
fi

# Check if cmake is installed
if ! command -v cmake &> /dev/null; then
    echo "cmake is not installed. Installing..."
    sudo apt install cmake > /dev/null
fi

# Check if gcc-arm-none-eabi is installed
if ! command -v arm-none-eabi-gcc &> /dev/null; then
    echo "gcc-arm-none-eabi is not installed. Installing..."
    sudo apt install gcc-arm-none-eabi > /dev/null
fi

# Check if libnewlib-arm-none-eabi is installed
if ! dpkg -l | grep -q libnewlib-arm-none-eabi; then
    echo "libnewlib-arm-none-eabi is not installed. Installing..."
    sudo apt install libnewlib-arm-none-eabi > /dev/null
fi

# Check if build-essential is installed
if ! dpkg -l | grep -q build-essential; then
    sudo apt install build-essential > /dev/null
fi

# Path to the file
file_path="/home/$USERNAME/sdmay24-33/emulator/build-hex-files/build/cmake_install.cmake"

# Extracting the string
user_name_replace=$(grep -oP '(?<=/home/)[^/]+' "$file_path" | awk 'NR==1{print $1}')

# Comparing usernames and performing find and replace
if [[ "$user_name_replace" != "$USERNAME" ]]; then
    find /home/"$USERNAME"/sdmay24-33/emulator -type f -not -name "emulator.sh" -exec sed -i "s/${user_name_replace}/${current_user}/g" {} \;
fi

# add cmake 'build' from vs code
/usr/bin/cmake --no-warn-unused-cli -DCMAKE_BUILD_TYPE:STRING=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE -DCMAKE_C_COMPILER:FILEPATH=/usr/bin/arm-none-eabi-gcc -DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/arm-none-eabi-g++ -S/home/$USERNAME/sdmay24-33/emulator/build-hex-files -B/home/$USERNAME/sdmay24-33/emulator/build-hex-files/build -G "Unix Makefiles" > /dev/null 2>&1

/usr/bin/cmake --build /home/$USERNAME/sdmay24-33/emulator/build-hex-files/build --config Debug --target all -j 7 -- > /dev/null 2>&1

# Navigate to sdmay24-33/emulator/build-hex-files/build
cd /home/"$USERNAME"/sdmay24-33/emulator/build-hex-files/build

# Copy the "build-hex-files.hex" file
cp build-hex-files.hex /home/"$USERNAME"/sdmay24-33/emulator/rp2040js/

# Navigate to the proper directory
cd /home/$USERNAME/sdmay24-33/emulator/rp2040js

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Installing..."
    sudo apt install nodejs > /dev/null
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "npm is not installed. Installing..."
    sudo apt install npm > /dev/null
fi

compare_versions() {
    # Get the current Node.js version
    local NODE_VERSION=$(node --version | cut -d v -f 2)
    # Compare the version with the provided version
    if [ "$(printf '%s\n' "$1" "$NODE_VERSION" | sort -V | head -n1)" != "$1" ]; then
        return 1
    else
        return 0
    fi
}

# Check Node.js version
if ! compare_versions "20.0"; then
    echo "Node.js version is less than 20.0. Please update to continue..."
    sudo npm install -g n > /dev/null
    sudo n latest > /dev/null
fi

# Install npm dependencies
npm install --silent > /dev/null

# Run npm start
timeout 5 npm start --silent > /home/$USERNAME/sdmay24-33/emulator/npm_output.txt

