import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

circle_array = list(range(1, n+1))

path = []
start_idx = 0
for _ in range(n):
    path.append(circle_array[start_idx])
    start_idx = (start_idx + m - 1) % n

result = ''.join(map(str, path))

print(result)
