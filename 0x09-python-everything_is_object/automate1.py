#!/usr/bin/python3
import os

def generate_answer_files(answers):
    for i in range(0, 29):
        with open(f"{i}-answer.txt", "w", encoding="utf-8") as f:
            f.write(answers[i])

def generate_other_files():
    with open("100-magic_string.py", "w") as f:
        f.write("def magic_string():\n\treturn 'magic'")
    with open("101-locked_class.py", "w") as f:
        f.write("class LockedClass:\n\tdef __init__(self):\n\t\tself.locked = True\n\tdef __setattr__(self, key, value):\n\t\tif key == 'locked':\n\t\t\traise AttributeError('locked is a read-only attribute')\n\t\telse:\n\t\t\tsuper().__setattr__(key, value)")
    with open("103-line1.txt", "w") as f:
        f.write("line 1")
    with open("103-line2.txt", "w") as f:
        f.write("line 2")
    with open("104-line1.txt", "w") as f:
        f.write("line 1")
    with open("104-line2.txt", "w") as f:
        f.write("line 2")
    with open("104-line3.txt", "w") as f:
        f.write("line 3")
    with open("104-line4.txt", "w") as f:
        f.write("line 4")
    with open("104-line5.txt", "w") as f:
        f.write("line 5")
    with open("105-line1.txt", "w") as f:
        f.write("line 1")
    with open("106-line1.txt", "w") as f:
        f.write("line 1")
    with open("106-line2.txt", "w") as f:
        f.write("line 2")
    with open("106-line3.txt", "w") as f:
        f.write("line 3")
    with open("106-line4.txt", "w") as f:
        f.write("line 4")
    with open("106-line5.txt", "w") as f:
        f.write("line 5")

if __name__ == "__main__":
    answers = [
    "type",
    "id",
    "No",
    "Yes",
    "Yes",
    "No",
    "True",
    "True",
    "True",
    "True",
    "True",
    "False",
    "True",
    "True",
    "[1, 2, 3, 4]",
    "[1, 2, 3]",
    "1",
    "[1, 2, 3, 4]",
    "[1, 2, 3]",
    "be py",
    "Yes",
    "Yes",
    "No",
    "Yes",
    "True",
    "False",
    "True",
    "No",
    "Yes",
    ]
    generate_answer_files(answers)
    generate_other_files()
