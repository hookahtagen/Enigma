import string

def poly_vigenere_encrypt(plaintext, key, alphabets):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char in alphabets[key[key_index % len(key)]]:
            char_index = alphabets[key[key_index % len(key)]].find(char)
            ciphertext += alphabets[key[key_index % len(key)]][(char_index + 1) % len(alphabets[key[key_index % len(key)]])]
        else:
            ciphertext += char
        key_index += 1
    return ciphertext

def poly_vigenere_decrypt(ciphertext, key, alphabets):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char in alphabets[key[key_index % len(key)]]:
            char_index = alphabets[key[key_index % len(key)]].find(char)
            plaintext += alphabets[key[key_index % len(key)]][(char_index - 1) % len(alphabets[key[key_index % len(key)]])]
        else:
            plaintext += char
        key_index += 1
    return plaintext

alphabets = {
    'A': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    'B': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    'C': 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
}
key = "AAABBB"

plaintext = "secret message"
ciphertext = poly_vigenere_encrypt(plaintext, key, alphabets)
print("Encrypted message: ", ciphertext)

decrypted_plaintext = poly_vigenere_decrypt(ciphertext, key, alphabets)
print("Decrypted message: ", decrypted_plaintext)