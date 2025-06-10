def reverse_list(lst):
    return lst[::-1]

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]

print("Reversed list:", reverse_list(my_list))
print("Rotated list (2 places to the right):", rotate_list(my_list, 2))
