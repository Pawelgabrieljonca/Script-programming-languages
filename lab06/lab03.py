try:
    x = int(input("Enter a number:"))
    result = 10 /x
except ValueError:#obsługa błędu konwersji na liczbe całkowita
    print("Something went wrong")
except ZeroDivisionError:#obłsuga dzielenia przez zero
    print("You can't divide by zero")
else: #ten blok wykona się jeśli nie wystąpi błąd
    print(f"Everything went fine {result}")
finally:#wykona się zawsze
    print("I dont't care whether something went wrong")
