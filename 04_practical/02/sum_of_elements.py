def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum of elements:", sum_of_elements(numbers))