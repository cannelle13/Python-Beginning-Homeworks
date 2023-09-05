with open("first.txt", "r") as file1:
    content_upper = file1.read().upper()

with open("second.txt", "w") as file2:
    file2.write(content_upper)
