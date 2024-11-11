def xor_encrypt_decrypt(plain_text, key):
    if len(plain_text) != len(key):
        raise ValueError("Długość tekstu jawnego i słowa szyfrującego musi być taka sama.")
    encrypted_text = ""
    for i in range(len(plain_text)):

        encrypted_char = ord(plain_text[i]) ^ ord(key[i]) # Pobieramy kod ASCII dla obu znaków i wykonujemy operację XOR

        encrypted_text += chr(encrypted_char)  # Konwertujemy wynik do znaku i dodajemy do wyniku
    return encrypted_text
def main():
    plain_text = "Paweljon"
    key = "kodykody"
    encrypted_text = xor_encrypt_decrypt(plain_text, key)# Szyfrowanie
    print(f"Tekst zaszyfrowany: {encrypted_text}")
    decrypted_text = xor_encrypt_decrypt(encrypted_text, key)# Deszyfrowanie
    print(f"Tekst odszyfrowany: {decrypted_text}")

if __name__ == "__main__":
    main()
