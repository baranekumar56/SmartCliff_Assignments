
n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

res = []

for i in range(n):

    j = i + 1
    k = len(nums) - 1

    while j < n and k >= 0 and j <= k:

        val = nums[i] + nums[j] + nums[k]

        if val < 0 :
            j += 1
        elif val > 0:
            k -= 1
        else :
            res.append([nums[i], nums[j], nums[k]])
            t1 = nums[j]
            t2 = nums[k]
            while nums[j] == t1:
                j += 1

            while nums[k] == t2:
                k-= 1


print(res)