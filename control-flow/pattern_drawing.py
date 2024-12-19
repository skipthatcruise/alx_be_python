pattern_size = int(input("Enter the size of the pattern: "))
rows = pattern_size + 1
i = 1
while i < rows:
    for pattern in range(1, 2):
        print(pattern_size * "*", end="")
        print()
        i+=1