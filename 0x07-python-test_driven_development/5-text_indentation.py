#!/usr/bin/python3
"""Function to print text with indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    current_line = ""
    punctuation = [".", "?", ":"]
    

    for char in text:
        current_line += char
        if char in punctuation:
            lines.append(current_line.strip())
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        line = line.replace(".", "").replace("?", "").replace(":", "")
        print(line)
