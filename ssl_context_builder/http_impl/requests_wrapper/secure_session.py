import weakref
import os
import requests
import ssl
from ssl import SSLContext
import logging

from ssl_context_builder.http_impl.requests_wrapper.ssl_adapter import SslAdapter


class RequestsSecureSession:

    def __init__(self, ssl_context: SSLContext):
        """
        This class create a wrapper for the requests.Session object
        It does the following:
        1. Disable session env_vars consuming
        2. Load certificates provided with the ssl_context
        3. Except ssl_context to control the TLS communication
        @param ssl_context: SSLContext
        """
        self.cert_file_path = self._create_cert_file(ssl_context)  # see note inside the function why not using tempfile
        self._ssl_context = ssl_context
        self.session = requests.Session()
        self.session.trust_env = False
        self.session.verify = self.cert_file_path
        self.session.mount('https://', SslAdapter(ssl_context))

        self._finalizer = weakref.finalize(
            self, self._cleanup, self.cert_file_path, self.session,
            warn_message="Implicitly cleaning up {!r}".format(self))

    def __enter__(self):
        return self

    def __exit__(self, exc, value, tb):
        self.cleanup()

    def cleanup(self):  # Non throw function
        """
        Delete the cert file and close the session
        @return:
        """
        if self._finalizer.detach():
            try:
                os.remove(self.cert_file_path)
            except:
                logging.warning(f"Couldn't delete certs file {self.cert_file_path}")

            try:
                self.session.close()
            except:
                logging.warning("Couldn't close session")

    @staticmethod
    def _cleanup(name, session, warn_message):
        try:
            os.remove(name)
        except:
            logging.warning(f"Couldn't delete certs file {name}")
        try:
            session.close()
        except:
            logging.warning("Couldn't close session")
        logging.warning(warn_message)

    @classmethod
    def _create_cert_file(cls, ssl_context: SSLContext):
        """
        This create a CA bundle file extracted from the ssl_context
        The reason we are creating a real file and deleting it is that this file is being opened later on
        in the requests flow. This means we have to close the file before it is being used
        tempfile is being destroyed when closed.
        @param ssl_context: ssl_context
        @return: path to the created ca_bundle file
        """
        path = "certs.pem"
        if os.path.exists(path):
            path = cls._generate_cert_file_path("certs")
        with open(path, mode="a+") as certs_file:
            certs = ""
            for der in ssl_context.get_ca_certs(True):
                certs += f"{ssl.DER_cert_to_PEM_cert(der)}\n"
            certs_file.write(certs)
        return path

    @classmethod
    def _generate_cert_file_path(cls, file_name: str, num=1):
        file_name_candidate = f"{file_name}({num}).pem"
        if os.path.exists(file_name_candidate):
            return cls._generate_cert_file_path(file_name, num + 1)
        return file_name_candidate
