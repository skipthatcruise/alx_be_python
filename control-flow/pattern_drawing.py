pattern_size = int(input("Enter the size of the pattern: "))
rows = 0
while rows < pattern_size:
    for _ in range(pattern_size):
        print("*", end="")
    print()
    rows+=1