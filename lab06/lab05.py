from io import UnsupportedOperation
# Test trybu 'a' - append (dopisywanie)
print("Testing mode 'a': append")
try:
    with open("test_append.txt", "a") as f:
        f.write("Appending content.\n")  # Dodaje zawartość do pliku (tworzy, jeśli plik nie istnieje)
    print("Mode 'a': Successfully appended to 'test_append.txt'")
except Exception as e:
    print(f"Mode 'a': Failed to append to 'test_append.txt' - {e}")
# Test trybu 'w' - write (nadpisywanie)
print("\nTesting mode 'w': write")
try:
    with open("test_write.txt", "w") as f:
        f.write("Writing new content.\n")  # Nadpisuje plik lub tworzy nowy
    print("Mode 'w': Successfully wrote to 'test_write.txt'")
except Exception as e:
    print(f"Mode 'w': Failed to write to 'test_write.txt' - {e}")

# Test trybu 'x' - exclusive creation (tworzenie nowego pliku)
print("\nTesting mode 'x': exclusive creation")
try:
    with open("test_exclusive.txt", "x") as f:
        f.write("Creating new file with content.\n")  # Tworzy plik, jeśli nie istnieje
    print("Mode 'x': Successfully created and wrote to 'test_exclusive.txt'")
except FileExistsError:
    print("Mode 'x': File 'test_exclusive.txt' already exists, cannot overwrite.")
except Exception as e:
    print(f"Mode 'x': Failed to create 'test_exclusive.txt' - {e}")

# Test próby zapisu do plików
print("\nTesting writing to files with each mode:")
try:
    # Próba zapisu do pliku otwartego w trybie 'r'
    print("Testing write in 'r' mode:")
    with open("test_append.txt", "r") as f:
        f.write("This will not work.")  # To spowoduje błąd
except UnsupportedOperation:
    print("Write operation failed: Cannot write to a file opened in 'r' mode.")
except Exception as e:
    print(f"Unexpected error: {e}")
