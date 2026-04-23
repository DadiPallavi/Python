def find_average(numbers):
    if len(numbers) == 0:
        return 0  
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40]
print(find_average(nums))  # Output: 25.0