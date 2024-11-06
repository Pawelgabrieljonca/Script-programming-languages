def new_list():
    list = [1,2,3,4,5,6,7,8,9,0]

    check = [num for num in list if num % 2 != 0]
    if check:
        smallest = min(list)
    else:
        smallest = None


    print("list of numbers",list)
    print("odd numbers",check)
    print("Smallest",smallest)

def main():
    new_list()

if __name__ == '__main__':
    main()