from pathlib import Path

SSLKEYLOGFILE = "SSLKEYLOGFILE"

ALLOWED_KEY_LENGTHS = [128, 256]
ALLOWED_CIPHER_MODES = ["cbc", "gcm"]
ALLOWED_SECURITY_LEVELS = range(1, 6)
ALLOWED_ENC_TYPES = ["aes", "chacha"]

WINDOWS_SUPPORTED_CERT_STORES = ["CA", "ROOT", "MY"]
KEYCHAIN_TYPES = {
            'root': "/System/Library/Keychains/SystemRootCertificates.keychain",
            'system': "/Library/Keychains/System.keychain",
            'user': f"{str(Path.home())}/Library/Keychains/login.keychain-db"}
