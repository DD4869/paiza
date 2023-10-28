def elevator_another():
    N = int(input())
    if 1 <= N <= 100:
        total_move = 0
        current_floor = 1
        for _ in range(N):
            next_floor = int(input())
            f_i = next_floor
            if 1 <= f_i <= 100:
                total_move += abs(next_floor - current_floor)
                # update current_floor
                current_floor = next_floor
        print(total_move)   

# runner
if __name__ == "__main__":
    elevator_another()