from typing import Iterable, List
from itertools import permutations
from cypher_text import message

'''https://projecteuler.net/problem=59 Each character on a computer is assigned a unique code and the preferred standard is ASCII (American 
Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107. 

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher 
text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65. 

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random 
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both 
"halves", it is impossible to decrypt the message. 

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If 
the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The 
balance for this method is using a sufficiently long password key for security, but short enough to be memorable. 

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (
right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the 
plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the 
original text. '''


def crypt_stream(key: bytes, data: bytes):
    size_key = len(key)
    size_data = len(data)
    for i in range(0, size_data):
        key_byte = key[i % size_key]
        data_byte = data[i]
        yield data_byte ^ key_byte


def crypt(key: bytes, data: bytes) -> bytes:
    return list(crypt_stream(key,data))


def to_bytes(text: str) -> List[int]:
    return [ord(b) for b in text]


def from_bytes(bs: List[int]) -> str:
    return bytes(bs).decode('ascii')

def potential_keys():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return [(l[0] + l[1] + l[2]) for l in permutations(letters,3)]

def looks_like_real_text(text:str):
    return ' the ' in text

def get_plaintext(encrypted):
    for key in potential_keys():
        key_bytes = to_bytes(key)
        plaintext_bytes = crypt(key_bytes, encrypted)
        plaintext = from_bytes(plaintext_bytes)
        if looks_like_real_text(plaintext):
          return plaintext
    return "Dunno"

def main():
    decrypted = get_plaintext(message)
    print(decrypted)


if __name__ == "__main__":
    main()
