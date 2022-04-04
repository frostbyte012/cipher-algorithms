def encipher(plainText, key):
    cipherText = ""
    for i in plainText:
        if ord(i) >= 65 and ord(i) <= 90:
            cipherText += chr(((ord(i) + key - 65) % 26) + 65)
        else:
            cipherText += chr(((ord(i) + key - 97) % 26) + 97)
    return cipherText


def decipher(cipherText, key):
    plainText = ""
    for i in cipherText:
        if ord(i) >= 65 and ord(i) <= 90:
            plainText += chr(((ord(i) - key - 65) % 26) + 65)
        else:
            plainText += chr(((ord(i) - key - 97) % 26) + 97)
    return plainText


if __name__ == "__main__":
    plainText = input()
    key = int(input())

    encryptedText = encipher(plainText, key)
    print(f"Encoded text: {encryptedText}")
    decryptedText = decipher(encryptedText, key)
    print(f"Decoded text: {decryptedText}")
