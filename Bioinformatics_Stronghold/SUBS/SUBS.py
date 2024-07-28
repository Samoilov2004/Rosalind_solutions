file_path = './SUBS_input.txt'

with open(file_path, 'r') as f:
    big_line = f.readline().strip()
    pattern = f.readline().strip()

positions = []
start = 0
while True:
    start = big_line.find(pattern, start)
    if start == -1:
        break
    positions.append(start + 1)  # Добавляем 1, чтобы получить 1-based индексы
    start += 1  # Сдвигаем позицию на 1, чтобы найти следующее вхождение

output_line = " ".join(map(str, positions))
print(output_line)

with open('./SUBS_output.txt', 'w') as f:
    f.write(output_line)