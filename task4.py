import sys

# Считываем содержимое файла
with open(sys.argv[1], 'r') as file:
    nums = [int(line.strip()) for line in file.readlines()]

# Находим максимальное и минимальное значения
max_num = max(nums)
min_num = min(nums)

# Инициализируем переменную moves
moves = 0

# Проходимся по каждому элементу и добавляем разницу в moves
for num in nums:
    moves += abs(num - max_num)
    moves += abs(num - min_num)

# Выводим moves
print(moves)