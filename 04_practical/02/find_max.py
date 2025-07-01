def find_max(lst):
    if not lst:
        return None

    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print("Maximum value:", find_max(numbers))