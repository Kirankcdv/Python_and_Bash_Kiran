# Write to a File

content = """Python and Bash Assignment

This file was created using Python file handling.
The program uses open() and write() to create and write content to a text file.
"""

with open("sample.txt", "w") as file:
    file.write(content)

print("Content successfully written to sample.txt")