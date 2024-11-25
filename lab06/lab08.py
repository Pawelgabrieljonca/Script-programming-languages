import random
def random_num(n, a, b, filename='random_numbers.txt'):
    #Function to generate n random numbers in the range <a, b> and save them to a file.
    if n <= 0:
        print("The number of random numbers (n) must be positive.")
        return
    if a >= b:
        print("Invalid range: a must be less than b.")
        return
    # Generowanie n losowych liczb
    random_numbers = [random.uniform(a, b) for _ in range(n)]
    # Zapisywanie liczb do pliku tekstowego
    with open(filename, 'w') as file:
        for number in random_numbers:
            file.write(f"{number}\n")
    print(f"{n} random numbers from the range {a} to {b} have been saved to the file {filename}.")

random_num(10, 1, 100, 'output.txt')
