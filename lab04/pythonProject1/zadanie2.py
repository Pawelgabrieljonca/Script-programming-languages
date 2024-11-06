def new_list():
    numbers = []
    while len(numbers) < 10:
        try:
            num = float(input("Write number(left {} to write: )".format(10 - len(numbers))))
            numbers.append(num)
        except ValueError:
            print("Failed, give number")

    numbers.sort()
    min_number = numbers[0]
    max_number = numbers[-1]
    #calculating the average
    no_negative_numbers = [num for num in numbers if num >= 0]
    average_negative = sum(no_negative_numbers) / len(no_negative_numbers) if no_negative_numbers else 0

    print("Numbers:", numbers)
    print("Min:", min_number)
    print("Max:", max_number)
    print("Average:", average_negative)

def main():
    new_list()

if __name__ == '__main__':
    main()
