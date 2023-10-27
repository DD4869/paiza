# send mail function
def send_mail(input_string):
    if 1 <= len(S) <= 100:
        num_of_pluses = len(input_string) + 2
        print("+"*num_of_pluses)
        print(f"+"+input_string+"+")
        print("+"*num_of_pluses)
# run module
if __name__ == '__main__':
    S = input("").strip()
    send_mail(S)