# TODO решите задачу
import json

filename = 'input.json'

def task() -> float:
    with open(filename) as file:
        json_data = json.load(file)
    list_values = [item["score"] * item["weight"] for item in json_data]
    return round(sum(list_values),3)

print(task())