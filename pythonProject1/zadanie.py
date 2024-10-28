def li():
    list0 = [] #definiowanie listy
    print(list0)
    list0.extend([6, 7, 8, 9, 10])
    first_two = list0[:2]
    print(first_two)
    print(list0[-2:])
    print(list0)
    print(len(list0))
    print(list0[::2])
    list0.append(50)
    list0.append("Hej")
    list0.sort()
    list0.pop()
    list0.reverse()
    list0.insert(2, 100)
    num = list0.count(13)
    print(num)
    print(list0)
def main():
    li()

if __name__ == '__main__':
    main()