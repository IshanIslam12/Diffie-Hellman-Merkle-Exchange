import base64
import os

G = 3
P = 0x00d20145714aed92b594a8a5a7ba1abad06825f0bcdda651d862f5add6ad2aab7893581a2241944564cb32625c5577aa1b37283ded38cc7018e6d2990e3a0f45b3

os.system("clear")
import secrets
private = secrets.randbelow(P)
#print(f"My private key is: {hex(private)}")

def fastpow(b, e, p):
  r = 1
  while e > 0:
    if e % 2 == 0:
        b = b*b % p
        e = e // 2
    else:
        r = r*b % p
        e = e - 1
  return r


public = fastpow(G, private, P)
#print(f"My public key is: {hex(public)}")





leaguePublic = 0x8fff5f11a4d135e091b4686102c4c79a2acc353f0380d2809993311470b25b40339c2bc61c03c2abc156e7104d0afb52e1da5c0d2b6faa67c8ab22e2ec1605ad

IshaPrivate = 0x024338022b750a59814f53d2ae4672a5d78a33b5a06b4e782ab95820a3745121f143a6972b0845c40f8227988fb605629d906cbe4393480279ba1ea28c2c466559

# Verify my own public vs private
IshanPublic = fastpow(G, IshaPrivate, P)
#print(f"Ishan's public key is: {hex(IshanPublic)}")

leagueSecret = fastpow(leaguePublic, IshaPrivate, P)
#print(f"Secret key with Professor League: {hex(leagueSecret)}")

leagueSecretBytes = leagueSecret.to_bytes(64, byteorder='big')
#print(f"Our shared key converted to bytes is (L): {leagueSecretBytes}")


def xorBytes(xs, ys):
  return bytes(x^y for x, y in zip(xs, ys))

def encryptBytes64(message, key):
     return base64.b64encode(xorBytes(message.encode(), key)).decode()

def decryptBytes64(message, key):
    return xorBytes(base64.b64decode(message), key).decode()

armored = encryptBytes64("Assignment Completed", leagueSecretBytes)
#print(f"Message to Prof. League: {armored}")

league_message= decryptBytes64("7tU8qPTkSqXV8QBi2cz2dvginvAMa/M4ZEXxWKwWTYrfJGPBuDsB", leagueSecretBytes)
print(league_message)

