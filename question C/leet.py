def leet(s):
    if 1 <= len(s) <= 100:
        s = s.replace('a', '4');
        s = s.replace('A', '4');
        s = s.replace('E', '3');
        s = s.replace('G', '6');
        s = s.replace('I', '1');
        s = s.replace('O', '0');
        s = s.replace('S', '5');
        s = s.replace('Z', '2');
        return s;    

# run module
if __name__ == '__main__':
    s = input("").strip();
    print(leet(s));