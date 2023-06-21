def solution(N):
    # N = int(input())
    bin_str = format(N, 'b')
    return bin_str

bin_str = solution(9)

print(bin_str.count(0))