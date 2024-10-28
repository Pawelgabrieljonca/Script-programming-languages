def new_set():
    # Definicja słownika
    car_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "new": False
    }
    # Pobieranie wartości z klucza 'model'
    x = car_dict["model"]
    print("Wartość klucza 'model' za pomocą []:", x)
    x = car_dict.get("model")
    print("Wartość klucza 'model' za pomocą get():", x)
    # Lista kluczy, wartości i par klucz-wartość
    print("Lista kluczy:", car_dict.keys())
    print("Lista wartości:", car_dict.values())
    print("Lista par klucz-wartość:", car_dict.items())
    # Dodanie nowej pary klucz-wartość
    car_dict["color"] = "white"
    print("Po dodaniu nowej pary ('color': 'white'):", car_dict)
    # Aktualizacja wartości klucza 'year'
    car_dict["year"] = 1963
    print("Po aktualizacji wartości klucza 'year' na 1963:", car_dict)
    # Sprawdzenie, czy klucz 'model' znajduje się w słowniku
    if "model" in car_dict:
        print("element found!")
    # Usunięcie elementu o kluczu 'model'
    car_dict.pop("model")
    print("Po usunięciu klucza 'model':", car_dict)

    # Usunięcie ostatnio dodanej pary klucz-wartość
    car_dict.popitem()
    print("Po usunięciu ostatniej pary klucz-wartość:", car_dict)

def main():
    new_set()

if __name__ == "__main__":
    main()