from Crypto.Cipher import AES
from Crypto import Random


random = Random.new()
key = random.read(AES.key_size[0])
