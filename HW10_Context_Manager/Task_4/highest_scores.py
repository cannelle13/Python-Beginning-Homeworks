import csv
import operator

data_list = []
file_path = "Task_3/scores.csv"
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    data_list = list(reader)


highest_scores = {}
for row in data_list:
    player = row["Player name"]
    score = int(row["Score"])
    if player not in highest_scores or score > highest_scores[player]:
        highest_scores[player] = score

highest_scores = dict(
    sorted(highest_scores.items(), key=operator.itemgetter(1), reverse=True)
)

with open("highest_scores.csv", "w") as hs:
    for player, highest_score in highest_scores.items():
        hs.write(f"{player}, {highest_score}\n")
