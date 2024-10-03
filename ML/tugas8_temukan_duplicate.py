some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1: # berapa kali value (contoh a) akan terjadi dalam list
        if value not in duplicates: # Untuk memunculkan satu nilai saja ('b' dan 'n') bukan ('b', 'b', 'n', 'n')
            duplicates.append(value)

print(duplicates) 