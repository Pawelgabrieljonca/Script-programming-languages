def new_set():
    my_set = {1,2,3,4,5}
    print("Początkowy zbiór", my_set)
    my_set.remove(3)
    my_set.discard(4)
    print("Po usunieciu",my_set)

    element = my_set.pop()
    print("usunieta metoda pop", element)
    print(my_set)
def main():
    new_set()

if __name__ == "__main__":
    main()