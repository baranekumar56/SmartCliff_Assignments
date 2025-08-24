
nums = list(map(int, input().split()))

def get_longest_consecutive_seq(nums):
    nums.sort()
    dic = {}

    lcs = 1

    for i in nums:
        if i-1 in dic:
            if i in dic:
                dic[i] = max(dic[i], dic[i-1] + 1)
            else :
                dic[i] = dic[i-1] + 1
            lcs = max(lcs, dic[i])
        else:
            dic[i] = 1

    return lcs

print(get_longest_consecutive_seq(nums))