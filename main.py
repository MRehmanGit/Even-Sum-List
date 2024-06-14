def sum_of_evens(nums: list) -> int:
    # Initialize sum to 0
    sum = 0
    # Iterate over each number in the list
    for i in range(len(nums)):
        # If the number is even, add it to the sum
        if nums[i] % 2 == 0:
                sum += nums[i]
        else:
            continue

    # Return the total sum of even numbers
    return sum

#test case:
list_value = [1,2,3,4,5,6]
value = sum_of_evens(list_value)
print(value)
