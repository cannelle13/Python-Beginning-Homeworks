import random
import string

alphabet = string.ascii_uppercase
summary_data = []

for letter in alphabet:
    filename = f"{letter}.txt"
    random_number = random.randint(1, 100)
    summary_data.append(f"{filename}: {random_number}")

with open("summary.txt", "w") as summary_file:
    summary_file.write("\n".join(summary_data))
