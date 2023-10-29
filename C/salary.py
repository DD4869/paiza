def salary():    
    input_data = input().split()
    X, Y, Z = int(input_data[0]), int(input_data[1]), int(input_data[2])
    if 0 <= X <= 3000 and 0 <= Y <= 3000 and 0 <= Z <= 3000:
        N = int(input())
        if 1 <= N <= 100:
            total_salary = 0 
            for _ in range(N):
                # S and T are start and end time
                S, T = map(int, input().split())
                # input_data = input().split()
                # S, T = int(input_data[0]), int(input_data[1])
                #  from S to T (get range and go to if loop for each hour then add them to total_salary)
                for hour in range(S, T):
                        if 9 <= hour < 17:
                            total_salary += X
                        elif 17 <= hour < 22:
                            total_salary += Y
                        else:
                            total_salary += Z   
            print(total_salary)         
            return total_salary
# runner
if __name__ == "__main__":
    salary()