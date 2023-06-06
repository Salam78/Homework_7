def caesar_cipher(text, shift):
    encrypted_text = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                ascii_offset = ord('a')
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

shift = int(input("Введите сдвиг шифрования: "))
text = input("Введите текст: ")

encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)
input("press any key to close window")
