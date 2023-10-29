def medicine(n, m):
    if 1 <= n <= 30:
        if 1 <= m <= 5:
            return n * m * 3

# run module
if __name__ == '__main__':
    n = int(input("").strip())
    m = int(input("").strip())
    print(medicine(n,m))