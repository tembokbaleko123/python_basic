# Mencari bilangan genap terbanyak

def highest_even(li):
    """Info: Return the highest even number in the list."""
    even_nums = [num for num in li if num % 2 == 0]
    return max(even_nums) if even_nums else None

print(highest_even([10,2,3,4,8,11]))

# Cara lain

def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
