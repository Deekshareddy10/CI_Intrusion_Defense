from Crypto.PublicKey import RSA

def main():
    # Generate RSA 2048-bit key pair
    key = RSA.generate(2048)

    # Export and save the private key
    private_key = key.export_key()
    with open("bob_private.pem", "wb") as f:
        f.write(private_key)

    # Export and save the public key
    public_key = key.publickey().export_key()
    with open("bob_public.pem", "wb") as f:
        f.write(public_key)

    print("RSA key pair generated successfully.")
    print("Files created: bob_private.pem, bob_public.pem")

if __name__ == "__main__":
    main()
