m, n = map(int, input().split())
bomb = int(input())
map_list = [[0] * n for _ in range(m)]  # استفاده از روش صحیح برای ایجاد لیست

# ثبت مختصات بمب‌ها
bomb_positions = []
for _ in range(bomb):
    a, b = map(int, input().split())
    map_list[a-1][b-1] = "*"
    bomb_positions.append((a-1, b-1))

# جهت چک کردن موقعیت های اطراف
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for a, b in bomb_positions:
    for da, db in directions:
        na, nb = a + da, b + db
        if 0 <= na < m and 0 <= nb < n and map_list[na][nb] != "*":
            map_list[na][nb] += 1

# چاپ نتیجه
for row in map_list:
    print(" ".join(map(str, row)))
