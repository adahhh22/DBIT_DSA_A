def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 1]
    print("Has duplicates:", has_duplicates(list))
    list_no_duplicates = [1, 2, 3, 4, 5]
    print("Has duplicates:", has_duplicates(list_no_duplicates))