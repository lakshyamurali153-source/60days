def move_zeroes(nums):
    """
    Moves all 0's to the end of the array in-place while maintaining 
    the relative order of the non-zero elements.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0

    return nums


if __name__ == "__main__":
    test_array = [0, 1, 0, 3, 12]
    print(f"Original Array: {test_array}")
    
    move_zeroes(test_array)
    print(f"Modified Array: {test_array}")