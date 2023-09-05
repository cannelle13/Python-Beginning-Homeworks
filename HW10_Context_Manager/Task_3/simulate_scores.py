import random
import csv

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
num_rounds = 100
results_list = []

for _ in range(num_rounds):
    for player in players:
        score = random.randint(0, 1000)
        player_data = {"Player name": player, "Score": score}
        results_list.append(player_data)

with open("scores.csv", "w") as file:
    header = ["Player name", "Score"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(results_list)
