import random, math

colormodes = {
    0: "Gray Scale",
    1: "Color"
}

resolutions = {
    0: "100x100",
    1: "320x240",
    2: "640x480",
    3: "1280x1024"
}

speeds = {
    0: "1 FPS",
    1: "30 FPS",
    2: "60 FPS",
    3: "120 FPS",
    4: "240 FPS"
}

interrupts = {
    0: "ONLY DATA interrupts enabled",
    1: "BOTH interrupts enabled"
}

def generate(data):
    colormode = random.choice(list(colormodes.keys()))
    resolution = random.choice(list(resolutions.keys()))
    speed = random.choice(list(speeds.keys()))
    interrupt = random.choice(list(interrupts.keys()))
    data['params']['colormode'] = colormodes[colormode]
    data['params']['resolution'] = resolutions[resolution]
    data['params']['speed'] = speeds[speed]
    data['params']['interrupts'] = interrupts[interrupt]

    configMask = (colormode << 6) | (resolution << 4) | (speed << 1) | 1
    intMask = 0x31 | (interrupt << 1)

    data['params']['masks'] = f"{configMask}\n{intMask}\n"

