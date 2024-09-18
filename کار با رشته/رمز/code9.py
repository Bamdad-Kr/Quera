number = int(input())
num = input()
count = 0

for i in range(0, number):
    password = input()
    password_r = password[::-1]

    if num[i] == '0' and password[0] == '0':
        count += 0
    elif num[i] in password:
        clockwise_index = password.index(num[i])
        counter_clockwise_index = password_r.index(num[i])

        if clockwise_index <= counter_clockwise_index:
            count += clockwise_index
        else:
            count += counter_clockwise_index + 1
    else:
        count = -1
        break

print(count)
