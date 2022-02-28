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

SSLv2 = "SSLv2"
SSLv3 = "SSLv3"
TLSv1 = "TLSv1"
TLSv1_1 = "TLSv1_1"
TLSv1_2 = "TLSv1_2"
TLSv1_3 = "TLSv1_3"
SUPPORTED_TLS_VERSIONS = [SSLv2, SSLv3, TLSv1, TLSv1_1, TLSv1_2, TLSv1_3]
