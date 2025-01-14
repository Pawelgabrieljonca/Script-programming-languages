import re
# Funkcja do odczytania pliku i przetworzenia go
def process_inwokacja_file():
    with open('inwokacja.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    # 1. Wypisać słowa, po których występuje „!”
    words_after = re.findall(r'\b\w+(?=\!)', text)
    print("Słowa, po których występuje '!':")
    print(words_after)

    # 2. Wypisać słowa z polskimi znakami
    polish_words = re.findall(r'\b\w*[\u0104\u0106\u0118\u0119\u0141\u0142\u0143\u015A\u015B\u0179\u017A\u017C\u017C\u00F3\u00F1\u00F3]\w*\b', text)
    print("\nSłowa z polskimi znakami:")
    print(polish_words)

    # 3. Zliczyć wystąpienia słowa "cię" lub "ci"
    ci_cie = len(re.findall(r'\bci[ęe]\b', text))
    print("\nLiczba wystąpień słowa 'cię' lub 'ci':")
    print(ci_cie)
# Uruchomienie funkcji
process_inwokacja_file()
