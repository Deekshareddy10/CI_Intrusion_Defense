from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import hmac, hashlib

def main():
    # Load Bob's public key
    with open("bob_public.pem", "rb") as f:
        bob_public_key = RSA.import_key(f.read())

    # Initialize RSA-OAEP using SHA256 from PyCryptodome
    rsa_cipher = PKCS1_OAEP.new(bob_public_key, hashAlgo=SHA256)

    # Read secret file
    with open("secret.txt", "rb") as f:
        plaintext = f.read()

    # Generate symmetric AES key, HMAC key, and IV
    aes_key = get_random_bytes(32)       # AES-256 key
    hmac_key = get_random_bytes(32)      # HMAC-SHA256 key
    iv = get_random_bytes(16)            # AES-CTR IV

    # AES-CTR Encryption
    aes_cipher = AES.new(aes_key, AES.MODE_CTR, nonce=b'', initial_value=iv)
    ciphertext = aes_cipher.encrypt(plaintext)

    # Compute HMAC over IV || ciphertext
    tag = hmac.new(hmac_key, iv + ciphertext, hashlib.sha256).digest()

    # Bundle AES key, HMAC key, and IV
    key_bundle = aes_key + hmac_key + iv

    # Encrypt (wrap) the key bundle using RSA-OAEP
    wrapped_keys = rsa_cipher.encrypt(key_bundle)

    # Save output files
    with open("ciphertext.bin", "wb") as f:
        f.write(iv + ciphertext)

    with open("tag.bin", "wb") as f:
        f.write(tag)

    with open("wrapped_keys.bin", "wb") as f:
        f.write(wrapped_keys)

    print("Encryption complete.")
    print("Generated files:")
    print(" - ciphertext.bin")
    print(" - tag.bin")
    print(" - wrapped_keys.bin")

if __name__ == "__main__":
    main()