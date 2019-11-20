def getPrintMaxAs(n):
    screen = [0] * (n + 1)

    for i in range(0, 6):  # till index 5
        screen[i] = i + 1
    for i in range(6, n):
        screen[i] = max(2 * screen[i - 3], 3 * screen[i - 4], 4 * screen[i - 5])
    return screen

print(getPrintMaxAs(20))
