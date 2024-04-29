import random


def generate(data):
    try:
        with open("answer.txt", 'r') as file:
            content = file.read()

            content_lower = content.lower()

            count = 0

            words_and_phrases = ["apple", "banana", "orange", "python", "programming"]


            for item in words_and_phrases:
                item_lower = item.lower()

                if item_lower in content_lower:
                    count += 1

    except FileNotFoundError:
        return None

    # Put the sum into data['correct_answers']
   # data["correct_answers"]["c"] = c
