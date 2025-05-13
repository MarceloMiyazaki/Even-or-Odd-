n = 0
for i in range(999999):
    x = "\nif n == "
    x += str(n)
    x += ": print(\"The number is even\")"
    y = "\nif n == "
    y += str(n+1)
    y += ": print(\"The number is odd\")"

    with open ("texto.txt","a") as file:
        file.write(x)
        file.write(y)
    n += 2