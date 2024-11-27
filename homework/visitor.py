# %%
from pathlib import Path

# RSA encryption modules from pycryptodome library
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Define paths for our key files
PROJECT_FOLDER = Path(__file__).parent.parent
# PRIVATE_KEY_FILE = PROJECT_FOLDER / "ceu_keypair"  # Contains the private key
PUBLIC_KEY_FILE = PROJECT_FOLDER / "ceu_keypair.pub"  # Contains the public key

# Make sure our key files exist before proceeding
# assert Path.exists(PRIVATE_KEY_FILE)
assert Path.exists(PUBLIC_KEY_FILE)

# %%
# Load the private key from file
# The private key must be kept secret and secure
with open(PUBLIC_KEY_FILE, "r", encoding="utf8") as key_file:
    public_key = RSA.import_key(key_file.read())

# %%
# Extract the public key from our private key
# The public key can be freely shared with anyone
# public_key = public_key.publickey()
print(f"Public key:\n{public_key.export_key().decode('utf-8')}")

# %%
# Message to be encrypted - must be converted to bytes
short_secret_message = "Max Pontot Kérünk.".encode("utf-8")

# Create a cipher object using the public key for encryption
public_key_cipher = PKCS1_OAEP.new(public_key)

# Encrypt our message - only someone with the private key can decrypt it
encrypted_message = public_key_cipher.encrypt(short_secret_message)
print("Encrypted message:")
print(encrypted_message)

# Save the encrypted message to a file
ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER / "visitor_message.bin"
with open(ENCRYPTED_MESSAGE_FILE, "wb") as f:
    f.write(encrypted_message)
