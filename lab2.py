def prime_num_generator():

    first_number = 2

    while True:
        is_first = True
        for num in range(2, int(first_number ** 0.5) + 1):
            if first_number % num == 0:
                is_first = False
                break

        if is_first:
            yield first_number
        first_number += 1

generator = prime_num_generator()

for i in range(5):
    print(next(generator))