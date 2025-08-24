
n = int(input())

nums = []

for i in range(0, 2*n):
    nums.append(int(input()))


# i denotes 0th index and j denotes n // 2 th index
# we iterate through the list , when index is odd we add element at i then increment it
# when it is odd we add element at j , and increment j by 1

def shuffle_list(nums):

    res = []
    n = len(nums)
    i = 0
    j = n // 2

    for k in range(0, n):
        if k % 2 == 0:
            res.append(nums[i])
            i += 1
        else :
            res.append(nums[j])
            j += 1


    return res

print(shuffle_list(nums))
