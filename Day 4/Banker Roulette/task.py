import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# option number 1
print(random.choice(friends)) # choice must have a sequence .choice(seq) will get error

# option 2
random_index = random.randint(0, 4) # selects a number from 0 - 4  as there are 5 elements in list
print(friends[random_index]) # uses number as index in friends and prints that name