def factory(n, h):
    if 1 <= n <= 200:
        if 1 <= h <= 24:
            return n * h
    else:
        return n

# run module
if __name__ == '__main__':
    n = int(input("").strip())
    h = int(input("").strip())
    print(factory(n, h))