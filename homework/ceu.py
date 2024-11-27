# %%
from pathlib import Path

# RSA encryption modules from pycryptodome library
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Define paths for our key files
PROJECT_FOLDER = Path(__file__).parent.parent
PRIVATE_KEY_FILE = PROJECT_FOLDER / "ceu_keypair"  # Contains the private key
PUBLIC_KEY_FILE = PROJECT_FOLDER / "ceu_keypair.pub"  # Contains the public key

# Make sure our key files exist before proceeding
assert Path.exists(PRIVATE_KEY_FILE)
assert Path.exists(PUBLIC_KEY_FILE)

# %%
# Load the private key from file
# The private key must be kept secret and secure
with open(PRIVATE_KEY_FILE, "r", encoding="utf8") as key_file:
    private_key = RSA.import_key(key_file.read())
# %%

# Extract the public key from our private key
# The public key can be freely shared with anyone
print(f"Private key:\n{private_key.export_key().decode('utf-8')}")

# %%
# Create a cipher object using the public key for encryption
private_key_cipher = PKCS1_OAEP.new(private_key)

# %%
# READ the encrypted message to a file
ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER / "visitor_message.bin"
with open(ENCRYPTED_MESSAGE_FILE, "rb") as f:
    decrypted_message = private_key_cipher.decrypt(f.read())
print("Encrypted message:")
print(decrypted_message.decode("utf-8"))
