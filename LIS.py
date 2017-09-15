
##Code for Longest increasing subsequence using dynamic programming
def lis(input_list):
    len_of_input = len(input_list)
    lis = [1] * len_of_input
    for i in range(1, len_of_input):
        for j in range(0, i):
            if input_list[i] > input_list[j] and lis[i] < (lis[j] + 1):
                lis[i] = lis[j] + 1
    return max(lis)

print(lis([10, 22, 9, 33, 21, 50, 41, 60]))
