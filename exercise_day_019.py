# 30DaysOfPython Exercises 


print("...................(""Exercise Level 1 (Q.1)"")............................")

import os

desktop = os.path.expanduser("~/Desktop")
print(desktop)


def count_lines_and_words(filename):
    with open(filename, "r") as file:
        text = file.read()

    lines = text.split('\n')
    num_lines = len(lines)

    words = text.split()
    num_words = len(words)

    return num_lines, num_words

desktop = "C:\Users\Lenovo\Desktop\Exercise_day_019"
files = ["obama_speech.txt", "michelle_obama_speech.txt", "donald_speech.txt", "melina_trump_speech.txt"]

for filename in files:
    filepath = os.path.join(folder, filename)
    num_lines, num_words = count_lines_and_words(filepath)
    print(filename)
    print("Number of lines:", num_lines)
    print("Number of words:", num_words)

