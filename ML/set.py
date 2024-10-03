mind_set = {
    1,2,3,4,5,5
}

print(mind_set)

# set method
my_set = {
    1,2,3,4,5
}

your_set = {
    4,5,6,7,8,9,10
}

print(my_set.difference(your_set))

print(my_set.discard(5))

print(my_set.difference_update(your_set)) # Mengubah perbedaan yang berarti menambah dikeduanya perbedaan yang ada

print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set)) # Mengembalikan nilai true jika ada kesamaan dan false jika tidak ada