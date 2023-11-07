def find_max_binary_ones(nums):
    max_count = 0
    result = None

    for num in nums:
        for other in nums:
            sumOfTwo = bin(num + other)
            print(f'num = {num}, other = {other}, sum = {sumOfTwo}')
            count_ones = sumOfTwo.count('1')
            if count_ones > max_count:
                max_count = count_ones
                result = (num, other)

    return result


numbers = [1, 3, 4, 6, 7, 5, 2]
result = find_max_binary_ones(numbers)
print(result)