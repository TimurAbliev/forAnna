import sys


def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Считывание координат центра окружности и радиуса из файла 1
with open(sys.argv[1], 'r') as file1:
    center_x = float(file1.readline())
    center_y = float(file1.readline())
    radius = float(file1.readline())

# Считывание координат точек из файла 2 и определение их положения относительно окружности
with open(sys.argv[2], 'r') as file2:
    for line in file2:
        point_x, point_y = map(float, line.strip())
        distance = calculate_distance(center_x, center_y, point_x, point_y)

        if distance == radius:
            print(0)
        elif distance < radius:
            print(1)
        else:
            print(2)