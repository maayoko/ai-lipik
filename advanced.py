# ROT13

# %% 5
string = "let go"


class Encryptor:
    NORMAL_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ROT13_ALPHA = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

    def __init__(self, string) -> None:
        self.string: str = string

    def encrypt(self) -> str:
        return self.string.translate(str.maketrans(self.NORMAL_ALPHA, self.ROT13_ALPHA))

    def decrypt(self, string: str):
        return string.translate(str.maketrans(self.ROT13_ALPHA, self.NORMAL_ALPHA))

    def display_ascii_chars(self) -> None:
        for char in self.string:
            print(ord(char))


encryptor = Encryptor(string)
encryptor.display_ascii_chars()
encrypted = encryptor.encrypt()
print(encrypted)
print(encryptor.decrypt(encrypted))

# %% 6
string = "idemo"
shift = 13


class Cipher:
    def __init__(self, shift) -> None:
        self.shift: int = shift
        self.unshift: int = 26 - shift

    def encrypt(self, string: str):
        return self.__cipher(string, self.shift)

    def decrypt(self, string: str):
        return self.__cipher(string, self.unshift)

    def __cipher(self, string: str, shift: int):
        ciphered_string = ""
        for char in string:
            if char.isupper():
                ciphered_string += chr((ord(char) +
                                        shift - 65) % 26 + 65)
            else:
                ciphered_string += chr((ord(char) +
                                        shift - 97) % 26 + 97)

        return ciphered_string


cipher = Cipher(shift)
encrypted = cipher.encrypt(string)
print(encrypted)
print(cipher.decrypt(encrypted))

# %% 7
