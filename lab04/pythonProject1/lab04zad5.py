class Item:
    def get_sound(self) -> None:
        print("item's sound")

class Element:
    def get_sound(self) -> None:
        print("element's sound")

class Thing(Element, Item):  # Dziedziczenie po dwóch klasach
    def say_hello(self) -> None:
        print("hello!")

# Tworzenie obiektów
item = Item()
element = Element()
thing = Thing()

# Wywołanie metody get_sound dla różnych obiektów
item.get_sound()     # Powinno wypisać "item's sound"
element.get_sound()  # Powinno wypisać "element's sound"
thing.get_sound()    # Powinno wypisać "element's sound" - metoda z klasy Element

# Zmiana kolejności klas bazowych
class ThingReversed(Item, Element):  # Dziedziczenie w odwrotnej kolejności
    def say_hello(self) -> None:
        print("hello!")

# Tworzenie obiektu typu ThingReversed
thing_reversed = ThingReversed()
thing_reversed.get_sound()  # Powinno wypisać "item's sound" - metoda z klasy Item
