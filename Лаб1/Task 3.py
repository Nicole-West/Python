list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)
index = count//2
team1 = list_players[:index]
team2 = list_players[index:]
print(team1)
print(team2)