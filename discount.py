# p is price, d is discount (1000 <= p <= 10000 then discounted, d = 100)
# return the price after discount
def discount(p):
    d = 100
    if 1000 <= p <= 10000:
        return p - d
    else:
        return p

# run module
if __name__ == '__main__':
    p = int(input("").strip())
    print(discount(p))