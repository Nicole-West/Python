numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i, value in enumerate(numbers):
    if numbers[i] is None:
        sum_ = sum(numbers[:i]) + sum(numbers[i+1:])
        count = len(numbers)
        averege_ = sum_/count
        numbers[i] = averege_
        break
print("Измененный список:", numbers)
