def traffic() :
    # input and split into N and M
    input_data = input().split()
    # get N and M from input_data
    N, M = int(input_data[0]), int(input_data[1])
    if 1 <= N <= 1000:
        total_traffic_length = 0
        for i in range(N - 1):
            A_i = int(input())
            if 1 <= A_i <= 200:
                if A_i <= M:
                    total_traffic_length += A_i
    print(total_traffic_length)
traffic()