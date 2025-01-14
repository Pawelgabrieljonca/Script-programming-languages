import re
def popraw_bledy_w_tekście(tekst):
    # Wzorzec do znalezienia błędnych słów
    pattern = r'\b([A-Z][A-Z][a-zA-Z]*)\b'
    def popraw_wyraz(match):
        word = match.group(1)
        # Zmieniam pierwszą literę na wielką, resztę na małe
        return word[0] + word[1:].lower()

    # Zamiana błędnych słów na poprawione
    up_text = re.sub(pattern, popraw_wyraz, tekst)
    return up_text
# Przykładowy tekst
text = "BYdgoszcz jest piękna. POlska to mój kraj. POlitechnika BYdgoska jest najlepsza."
# Popraw błędy w tekście
up_text = popraw_bledy_w_tekście(text)
print("Poprawiony tekst:", up_text)
