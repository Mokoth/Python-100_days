def main():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    print(f"{add(n, m):,}") # some locale formating
    
    # rounding to 2dp
    print(f"{add(n, m):.2f}")

def add(x, y):
    return x + y 

main()