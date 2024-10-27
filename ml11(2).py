import json
import math
with open('C:\\Artem`s Projects\\lab11\\coordinates.json', 'r') as file:
    data = json.load(file)
lengths = []
for s, points in data.items():
    x1, y1 = points[0]
    x2, y2 = points[1]
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    lengths.append((s, length))
longest = max(lengths, key=lambda x: x[1])
shortest = min(lengths, key=lambda x: x[1])
print(f"Найдовший відрізок: {longest[0]} з довжиною {longest[1]}")
print(f"Найкоротший відрізок: {shortest[0]} з довжиною {shortest[1]}")
