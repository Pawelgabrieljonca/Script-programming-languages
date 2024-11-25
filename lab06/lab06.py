import os
def display_directory_tree(start_path, indent_level=0):
    """
    Wyświetla drzewo katalogów dla wybranego katalogu.
    :param start_path: Ścieżka do katalogu początkowego
    :param indent_level: Poziom wcięcia (używany dla rekurencji)
    """
    if not os.path.exists(start_path):
        print("The specified path does not exist.")
        return
    if not os.path.isdir(start_path):
        print(f"The specified path '{start_path}' is not a directory.")
        return
    if indent_level == 0:    # Wyświetlenie katalogu głównego
        print(f"Directory tree for: {start_path}")
    # Iteracja przez zawartość katalogu
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        print("    " * indent_level + f"|-- {item}")
        # Jeśli element jest katalogiem, rekurencyjnie wyświetl jego zawartość
        if os.path.isdir(item_path):
            display_directory_tree(item_path, indent_level + 1)
# Przykładowe użycie
directory_to_explore = input("Enter the directory path to display its tree: ").strip()
display_directory_tree(directory_to_explore)
