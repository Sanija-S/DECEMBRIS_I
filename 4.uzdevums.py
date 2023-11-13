def faktorials(n):
    rezultats = 1
 
    for i in range(1, n + 1):
        rezultats *= i
 
    return rezultats

n = int(input("Ievadiet veselu pozitīvu skaitli: "))
 
print(f"Faktoriāls no {n} ir {faktorials(n)}.")

