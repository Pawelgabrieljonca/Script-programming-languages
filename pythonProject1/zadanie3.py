
def new_list():
    list1 = [1,2,3,4,5]
    list2 = [3,4,5,6,7]

    unique_item = [item for item in list1 if item not in list2]
    print(list1)
    print(list2)
    print(unique_item)


def main():
    new_list()

if __name__ == '__main__':
    main()