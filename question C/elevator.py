def elevator():
    log_lines = input().split()
    N = int(log_lines[0])
    if 1 <= N <= 100:
        total_move = 0
        f_i_list = []
        first_flag = True
        for i in range(N):
            f_i = int(input())
            f_i_list.append(f_i)
            if first_flag and 1 <= f_i <= 100:
                # elevetor goes up N - f_i floors
                total_move += f_i - 1
                # print(f"first:{total_move}")
                first_flag = False
            elif 1 <= f_i <= 100 and f_i > f_i_list[i-1]:
                # elevator goes down f_i - 1 floors
                total_move += f_i - f_i_list[i-1]
                # print(f"second:{total_move}")
            elif 1 <= f_i <= 100 and f_i < f_i_list[i-1]:
                # elevator goes up f_i - 1 floors
                total_move += f_i_list[i-1] - f_i
                # print(f"third:{total_move}")
            elif 1 <= f_i <= 100 and f_i == f_i_list[i-1]:
                # elevator stays
                total_move += 0    
                # print(f"forth:{total_move}")            
        print(total_move)   

# runner
if __name__ == "__main__":
    elevator()