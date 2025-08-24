
nums = list(map(int, input().split(" ")))


# iterate through each element and check nums[i] % 10 == i
def get_smallest_index_with_equal_value(nums):

    for i in range(0, len(nums)):

        if nums[i] % 10 == i:
            return i

    return -1

print(get_smallest_index_with_equal_value(nums))