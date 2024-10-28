def new_set():
    # Definiowanie dwóch zbiorów
    the_set = {1, 2, 3, 4, 5}
    this_set = {4, 5, 6, 7, 8}

    # a. Sprawdzenie, czy zbiory są rozłączne
    is_disjoint = the_set.isdisjoint(this_set)
    print("a. the_set.isdisjoint(this_set):", is_disjoint, "- typ:", type(is_disjoint))

    # b. Sprawdzenie, czy the_set jest podzbiorem this_set
    is_subset = the_set.issubset(this_set)
    print("b. the_set.issubset(this_set):", is_subset, "- typ:", type(is_subset))

    # c. Sprawdzenie, czy the_set jest nadzbiorem this_set
    is_superset = the_set.issuperset(this_set)
    print("c. the_set.issuperset(this_set):", is_superset, "- typ:", type(is_superset))

    # d. Połączenie obu zbiorów
    union_set = the_set.union(this_set)
    print("d. the_set.union(this_set):", union_set, "- typ:", type(union_set))

    # e. Różnica zbiorów
    difference_set = the_set.difference(this_set)
    print("e. the_set.difference(this_set):", difference_set, "- typ:", type(difference_set))

    # f. Przecięcie zbiorów
    intersection_set = the_set.intersection(this_set)
    print("f. the_set.intersection(this_set):", intersection_set, "- typ:", type(intersection_set))

def main():
    new_set()

if __name__ == "__main__":
    main()