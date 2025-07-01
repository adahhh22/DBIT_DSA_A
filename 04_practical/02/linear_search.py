def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

if __name__ == "__main__":  
    numbers = [20, 60, 55, 50, 90]
    target = 55
    result = linear_search(numbers, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")