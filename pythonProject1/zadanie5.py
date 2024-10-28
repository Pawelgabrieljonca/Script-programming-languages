def new_list():
    list_A = [1, 2, 3]
    list_B = ['a', 'b', 'c']

    combined_A_first = list_A + list_B
    print(combined_A_first)
    combined_B_first = list_B + list_A
    print(combined_B_first)

def main():
    new_list()

if __name__ == '__main__':
    main()