def unique_list():
    numbers = []
    print("Write numbers")
    while True:
        try:
            num = int(input())
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Please write correct number")
    unique_numbers = set(numbers)
    print("Unique numbers:",unique_numbers)
def main():
    unique_list()

if __name__ == '__main__':
    main()