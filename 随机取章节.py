import random
random_book_count = []
list80 = []
list40 = []
for i in range(80):
    list80.append(i)
random_book_count.extend(random.sample(list80, 6))
for i in range(80,121):
    list40.append(i)
random_book_count.extend(random.sample(list40, 3))
print(random_book_count)