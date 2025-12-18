from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import hmac, hashlib

def main():
    # Load Bob's private key
    with open("bob_private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    # Initialize RSA-OAEP with SHA256
    rsa_cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)

    # Load wrapped symmetric keys
    with open("wrapped_keys.bin", "rb") as f:
        wrapped_keys = f.read()

    # Load ciphertext (IV + encrypted bytes)
    with open("ciphertext.bin", "rb") as f:
        ciphertext_file = f.read()

    # Load HMAC tag
    with open("tag.bin", "rb") as f:
        tag_file = f.read()

    # Unwrap the symmetric keys + IV
    key_bundle = rsa_cipher.decrypt(wrapped_keys)
    aes_key = key_bundle[:32]
    hmac_key = key_bundle[32:64]
    iv = key_bundle[64:80]

    # Extract ciphertext from file
    ciphertext = ciphertext_file[16:]

    # Recompute expected HMAC
    expected_tag = hmac.new(hmac_key, iv + ciphertext, hashlib.sha256).digest()

    # Verify integrity
    if expected_tag != tag_file:
        print("Integrity check failed! Ciphertext may have been modified.")
        return

    # AES-CTR decryption
    aes_cipher = AES.new(aes_key, AES.MODE_CTR, nonce=b'', initial_value=iv)
    plaintext = aes_cipher.decrypt(ciphertext)

    # Save decrypted output
    with open("decrypted.txt", "wb") as f:
        f.write(plaintext)

    print("Decryption successful.")
    print("Decrypted output saved to decrypted.txt")

if __name__ == "__main__":
    main()
