

tuple = ("apple", "banana", "cherry")
tuple_b = ("orange",)
tuple += tuple_b #dodawanie krotek
multi_tuple = tuple * 2 #mnożenie krotek
print(len(tuple)) #długość krotki - liczba elementów
for x in tuple: #wypisanie wszystkich elementów krotki
    print(x)
