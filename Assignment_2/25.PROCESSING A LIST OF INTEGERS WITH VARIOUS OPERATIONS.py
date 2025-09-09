

def menu():
    n = int(input())
    nums = list(map(int, input().split()))

    print("Enter 1 for Removing duplicates from the list")
    print("Enter 2 for sum of unique values in the list")
    print("Enter 3 for mean of unique values in the list")
    print("Enter 4 for finding largest and smallest unique value in the list")
    print("Enter 5 for exiting the program")

    choice = int(input())

    match choice:

        case 1:
            nums = set(nums)
            print("Without Duplicates: ", nums)

        case 2:
            summ = sum(set(nums))
            print("Sum of unique values: ", summ)

        case 3:
            meann = sum(set(nums)) / len(nums)
            print("Mean of Unique values: ", meann)

        case 4:
            uni = set(nums)
            max_e = max(uni)
            min_e = min(uni)
            print("Max element in the list : {}\n Min Element in the list: {}".format(max_e, min_e))

        case 5:
            exit()

if __name__ == "__main__"
    menu()