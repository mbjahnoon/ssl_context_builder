import logging
import os
import ssl
import subprocess

from ssl_context_builder.builder.decorators import windows_only, macos_only
from ssl_context_builder.builder.constants import SSLKEYLOGFILE, ALLOWED_KEY_LENGTHS, ALLOWED_CIPHER_MODES, \
    ALLOWED_SECURITY_LEVELS, ALLOWED_ENC_TYPES, WINDOWS_SUPPORTED_CERT_STORES, KEYCHAIN_TYPES, SSLv2, SSLv3, TLSv1, \
    TLSv1_1, TLSv1_2, TLSv1_3, SUPPORTED_TLS_VERSIONS

__version__ = "0.0.1"


class SslContextBuilder:

    def __init__(self):
        """
        Init the Builder.
        initialize the ssl_context and load default certs
        """
        self._ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        self._ctx.load_default_certs()

    def build(self) -> ssl.SSLContext:
        """
        Return the SSL context after it being configured by the builder
        @return: ssl.SSLContext
        """
        return self._ctx

    def disable_key_logging(self):
        """
        Make sure no TLS keys are being logged
        @return: SslContextBuilder
        """
        del os.environ[SSLKEYLOGFILE]
        return self

    def set_key_logging(self, path: str):
        """
        WARNING: Only for debugging purpose
        Enable key logging for TLS session
        @param path: The path for which the TLS keys are logged to
        @return: SslContextBuilder
        """
        os.environ[SSLKEYLOGFILE] = path
        return self

    def disable_session_ticket(self):
        """
        Prevent client side from requesting a session ticket.
        @return: SslContextBuilder
        """
        self._ctx.options |= ssl.OP_NO_TICKET
        return self

    def chek_hostname_and_common_name(self):
        """
        Make sure hostname and common name will be validate in the retrieving certificate
        @return: SslContextBuilder
        """
        self._ctx.check_hostname = True
        self._ctx.hostname_checks_common_name = True
        return self

    def disable_renegotiation(self):
        """
        Disable all renegotiation in TLSv1.2 and earlier
        @return: SslContextBuilder
        """
        self._ctx.options |= ssl.OP_NO_RENEGOTIATION
        return self

    def use_max_key_length(self):
        """
         Make sure we are using key length of the size of 256 bit for symmetric encryption
         @return: SslContextBuilder
        """
        return self.set_key_length(max(ALLOWED_KEY_LENGTHS))

    def set_key_length(self, *key_lengths: int):
        """
        Set the symmetric key length
        NOTE: TLSv1_3 ciphers cannot be removed
        @param key_lengths: [128,256]
        @return: SslContextBuilder
        """
        for key_length in key_lengths:
            if key_length not in ALLOWED_KEY_LENGTHS:
                logging.error("Invalid key length %s", str(key_length))
                raise ValueError(f"Invalid key length {key_length}")
        if getattr(self._ctx, 'get_ciphers'):
            ciphers = [cipher["name"] for cipher in self._ctx.get_ciphers() if cipher["alg_bits"] in key_lengths]
            self._ctx.set_ciphers(":".join(ciphers))
            if not len(ciphers):
                raise RuntimeError(f"No ciphers found for key length: {key_lengths}")
        else:
            logging.warning("Couldn't set key length. _ssl.SslContext doesn't support 'get_ciphers'")
        return self

    def set_cipher_mode(self, *modes: str):
        """
        Set the cipher mode of the symmetric encryption
        @param modes: ["cbc", "gcm"]
        @return: SslContextBuilder
        """
        # NOTE: TLSv1_3 ciphers cannot be removed
        modes = [mode.lower() for mode in modes]

        for mode in modes:
            if mode not in ALLOWED_CIPHER_MODES:
                logging.error("Invalid cipher mode %s, ", mode)
                raise ValueError(f"Invalid key length {mode}")

        if getattr(self._ctx, 'get_ciphers'):
            ciphers = [cipher["name"] for cipher in self._ctx.get_ciphers() if
                       any(cipher["symmetric"].find(mode) > 0 for mode in modes)]
            if len(ciphers):
                self._ctx.set_ciphers(":".join(ciphers))
        else:
            logging.warning("Couldn't set key length. _ssl.SslContext doesn't support 'get_ciphers'")
        return self

    def set_maximum_key_exchange_security_level(self):  # Non throw
        """
        Set the key_exchange security properties to maximum
        @return: SslContextBuilder
        """
        return self.set_key_exchange_security_level(max(ALLOWED_SECURITY_LEVELS))

    def set_key_exchange_security_level(self, level: int):  # Non throw
        """
        Set the key_exchange security properties to the given level.
        the security level affects keyLength, TLS versions, allowed ciphers and more
        more information here: https://www.openssl.org/docs/man1.1.1/man3/SSL_CTX_set_security_level.html
        @param level: [1-5]
        @return: SslContextBuilder
        """
        try:
            if level not in ALLOWED_SECURITY_LEVELS:
                logging.error("Invalid security level. security Level should be an int in the range of 1-5")
            if level < self._ctx.security_level:
                logging.warning("Security level of the SSL connection ha been downgraded")
            self._ctx.set_ciphers(f'DEFAULT@SECLEVEL={level}')
            return self
        except Exception as e:
            logging.warning(
                f"Failed to set_key_exchange_security_level. "
                f"This feature is supported from openssl 1.1.0 and above. Exception: {e}")

    def set_cipher_type(self, *types: str):
        """
        Set the cipher type of the symmetric encryption
        @param types: ["aes", "chacha"]
        @return: SslContextBuilder
        """
        # NOTE: TLSv1_3 ciphers cannot be removed
        types = [cipher_type.lower() for cipher_type in types]
        for cipher_type in types:
            if cipher_type not in ALLOWED_ENC_TYPES:
                logging.error("Invalid cipher mode %s, ", cipher_type)
                raise ValueError(f"Invalid key length {cipher_type}")

        if getattr(self._ctx, 'get_ciphers'):
            ciphers = [cipher["name"] for cipher in self._ctx.get_ciphers() if
                       any(cipher["symmetric"].find(cipher_type) > -1 for cipher_type in types)]
            if not len(ciphers):
                return self
                # raise RuntimeError(f"No ciphers found for modes: {modes}")
            self._ctx.set_ciphers(":".join(ciphers))
        else:
            logging.warning("Couldn't set key length. _ssl.SslContext doesn't support 'get_ciphers'")
        return self

    # Configure TLS version
    def set_min_version(self, version: str):
        """
        Set the minimum TLS version to use
        @param version: [SSLv2, SSLv3, TLSv1, TLSv1_1, TLSv1_2, TLSv1_3]
        @return:SslContextBuilder
        """
        if version not in SUPPORTED_TLS_VERSIONS:
            logging.error("Invalid TLS version %s, ", version)
            raise ValueError(f"Invalid TLS version {version}")
        if version == SSLv2:
            self._ctx.minimum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
        elif version == SSLv3:
            self._ctx.minimum_version = ssl.TLSVersion.SSLv3
        elif version == TLSv1:
            self._ctx.minimum_version = ssl.TLSVersion.TLSv1
        elif version == TLSv1_1:
            self._ctx.minimum_version = ssl.TLSVersion.TLSv1_1
        elif version == TLSv1_2:
            self._ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        elif version == TLSv1_3:
            self._ctx.minimum_version = ssl.TLSVersion.TLSv1_3
        else:
            raise ValueError(f"unknown version: {version}")
        return self

    def set_max_version(self, version: str):
        """
        Set the maximum TLS version to use
        @param version: [SSLv2, SSLv3, TLSv1, TLSv1_1, TLSv1_2, TLSv1_3]
        @return:SslContextBuilder
        """
        if version not in SUPPORTED_TLS_VERSIONS:
            logging.error("Invalid TLS version %s, ", version)
            raise ValueError(f"Invalid TLS version {version}")
        if version == SSLv2:
            self._ctx.maximum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
        elif version == SSLv3:
            self._ctx.maximum_version = ssl.TLSVersion.SSLv3
        elif version == TLSv1:
            self._ctx.maximum_version = ssl.TLSVersion.TLSv1
        elif version == TLSv1_1:
            self._ctx.maximum_version = ssl.TLSVersion.TLSv1_1
        elif version == TLSv1_2:
            self._ctx.maximum_version = ssl.TLSVersion.TLSv1_2
        elif version == TLSv1_3:
            self._ctx.maximum_version = ssl.TLSVersion.TLSv1_3
        else:
            raise ValueError(f"unknown version: {version}")
        return self

    def use_tls_1_2_and_above(self):
        """
        Set the TLS versions to be 1_2 and above
        @return: SslContextBuilder
        """
        self.set_min_version(TLSv1_2)
        self.set_max_version(TLSv1_3)
        return self

    def use_minimum_tls_version(self):
        """
        Set the TLS versions to be SSLv2 and above
        @return: SslContextBuilder
        """
        self.set_min_version(SSLv2)
        self.set_max_version(TLSv1_3)
        return self

    def whitelist_application_layer_protocols(self, *protocols):
        """
        Set the allowed Network protocols to be allowed after the TLS handshake
        @param protocols: application layers protocols such as ['http/1.1', 'spdy/2']
        @return:SslContextBuilder
        """
        if ssl.HAS_ALPN:
            self._ctx.set_alpn_protocols(protocols)
        else:
            logging.warning("whitelist_application_layer_protocols is not supported by the ssl version.skipping...")
        return self

    def set_post_handshake_auth(self, value: bool):
        """
        Enable or Disable TLS 1.3 post-handshake client authentication
        @param value: True to enable. and False to disable
        @return: SslContextBuilder
        """
        self._ctx.post_handshake_auth = value
        return self

    # Load certs
    def use_default_certs(self):
        """
        Load the openssl default certs.
        Note - This will not load certs in macos
        This function will not raise indication in case of failure
        @return: SslContextBuilder
        """

        self._ctx.set_default_verify_paths()
        return self

    def use_crl(self):
        """
        Not implemented
        @return: SslContextBuilder
        """
        logging.warning("CRL is not implemented")
        return self

    @windows_only
    def use_windows_os_cert(self, store_name: str):
        """
        Load the RootCA from windows selected cert store
        @param store_name: ["CA", "ROOT", "MY"]
        @return: SslContextBuilder
        """
        if store_name not in WINDOWS_SUPPORTED_CERT_STORES:
            raise ValueError("Invalid win32 store name, store name must be one of %s",
                             ",".join(WINDOWS_SUPPORTED_CERT_STORES))
        certs = bytearray()
        for cert, encoding, trust in ssl.enum_certificates(store_name):
            # CA certs are never PKCS#7 encoded
            if encoding == "x509_asn":
                if trust is True:
                    certs.extend(cert)
        self._ctx.load_verify_locations(cadata=certs)
        return self

    @macos_only
    def use_mac_os_cert(self, keychain_type: str = None, key_chain_path: str = None):
        """
        Load the RootCA from macos selected cert store
        @param keychain_type: [root,system,user]
        @param key_chain_path: custom key chain that store certificates
        @return:
        """
        if keychain_type and keychain_type not in KEYCHAIN_TYPES.keys():
            logging.error("Error using macOS trust store cert. keychain_tyoe must be from the followings: %s",
                          ",".join(KEYCHAIN_TYPES.items()))
            raise ValueError(
                f"Error using macOS trust store cert. keychain_tyoe must be from the followings: "
                f"{','.join(KEYCHAIN_TYPES.items())}")
        keychain = None
        if keychain_type is not None:
            keychain = KEYCHAIN_TYPES[keychain_type]
        if key_chain_path is not None:
            keychain = key_chain_path
        self._load_mac_certs_from_keychain(keychain)
        return self

    def _load_mac_certs_from_keychain(self, keychain: str) -> None:
        """
        Using Command line to fetch certificates.
        @param keychain:
        @return:
        """
        if not os.path.exists(keychain):
            logging.warning("Can't find keychain %s in the machine."
                            " This is dangerous operation that could lead to remote code execution. Abborting...,",
                            keychain)
            return
        logging.debug("Get CA certs from mac keychain")
        try:
            get_ca_certs_process = subprocess.run(
                ["security", "find-certificate", "-a", "-p", keychain],
                capture_output=True,
                timeout=10,
                check=True,
                text=True)
            if get_ca_certs_process.returncode != 0:
                logging.warning("Couldn't retrieve ca certs for keychain: %s", keychain)
                return
            certs = get_ca_certs_process.stdout
            self._ctx.load_verify_locations(cadata=certs)

        except Exception as err:
            logging.warning("Got an error while trying to extract certificate from keychain")
