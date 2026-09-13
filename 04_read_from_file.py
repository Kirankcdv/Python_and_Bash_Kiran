# Read from a File

with open("sample.txt", "r") as file:
    content = file.read()

print("Content of sample.txt:")
print("----------------------")
print(content)