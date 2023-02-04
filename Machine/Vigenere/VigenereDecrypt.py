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
key = "BCACBA"
ciphertext = "IIJTAO UKQIIZI"

decrypted_plaintext = poly_vigenere_decrypt(ciphertext, key, alphabets)
print("Decrypted message: ", decrypted_plaintext)