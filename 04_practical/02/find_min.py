def find_min(lst):
    if not lst:
        return None

    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print("Minimum value:", find_min(numbers))