from typing import Iterable, List
from itertools import permutations
try:
    from .cypher_text import message
except:
    from cypher_text import message


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
