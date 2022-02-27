import weakref
import os
import requests
import ssl
from ssl import SSLContext
import logging

from ssl_context_builder.ssl_context_builder.builder import SslContextBuilder
from ssl_context_builder.ssl_context_builder.http_impl.requests_wrapper.ssl_adapter import SslAdapter


class RequestsSecureSession:
    def __init__(self, ssl_context: SSLContext):
        self.cert_file_path = self._create_cert_file(ssl_context)
        self._finalizer = weakref.finalize(
            self, self._cleanup, self.cert_file_path,
            warn_message="Implicitly cleaning up {!r}".format(self))
        self._ssl_context = ssl_context
        self.session = requests.Session()
        self.session.trust_env = False
        self.session.verify = self.cert_file_path
        self.session.mount('https://', SslAdapter(ssl_context))

    def __enter__(self):
        return self.session

    def __exit__(self, exc, value, tb):
        self.cleanup()

    def cleanup(self):
        if self._finalizer.detach():
            try:
                os.remove(self.cert_file_path)
            except:
                logging.warning(f"Couldn't delete certs file {self.cert_file_path}")

    @staticmethod
    def _cleanup(name, warn_message):
        try:
            os.remove(name)
        except:
            logging.warning(f"Couldn't delete certs file {name}")
        logging.warning(warn_message)

    @classmethod
    def _create_cert_file(cls, ssl_context: SSLContext):
        path = "certs.pem"
        if os.path.exists(path):
            path = cls._generate_cert_file_path("certs")
        with open(path, mode="a+") as certs_file:
            certs = ""
            for der in ssl_context.get_ca_certs(True):
                certs += f"{ssl.DER_cert_to_PEM_cert(der)}\n"
            certs_file.write(certs)
            certs_file.seek(0)
        return path

    @classmethod
    def _generate_cert_file_path(cls, file_name: str, num=1):
        file_name_candidate = f"{file_name}({num}).pem"
        if os.path.exists(file_name_candidate):
            return cls._generate_cert_file_path(file_name, num + 1)
        return file_name_candidate


if __name__ == '__main__':
    ctx = SslContextBuilder().build()
    s = RequestsSecureSession(ctx)
    print(s.session.get("https://google.com"))
    ctx.get_ca_certs()