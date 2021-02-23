def b_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


if __name__ == '__main__':
    list_of_nums = [35, 2, 1, 7, 0, 10, 121, 27]
    b_sort(list_of_nums)
    print(list_of_nums)
