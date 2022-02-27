import requests
from requests.adapters import HTTPAdapter
from ssl import SSLContext

from ssl_context_builder.ssl_context_builder.builder import SslContextBuilder


class SslAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests.
    """

    def __init__(self, ssl_context):
        self._custom_ssl = ssl_context
        super().__init__()

    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'] = self._custom_ssl
        return super(SslAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        kwargs['ssl_context'] = self._custom_ssl
        return super(SslAdapter, self).proxy_manager_for(*args, **kwargs)


def get_requests_session(ssl_context: SSLContext):
    from tempfile import NamedTemporaryFile, TemporaryFile
    import os
    certs_file = TemporaryFile(mode='r+',delete=False)
    os.chmod(certs_file.name, 777)
    certs = ""
    for der in ssl_context.get_ca_certs(True):
        certs += f"{ssl.DER_cert_to_PEM_cert(der)}\n"
    certs_file.write(certs)
    certs_file.seek(0)

    print(certs_file.name)
    print(certs_file.readable())
    s = requests.Session()
    s.trust_env = False
    s.verify = certs_file.name
    s.mount('https://', SslAdapter(ssl_context))
    print(s.get("https://google.com"))
    return s


builder = SslContextBuilder()
ctx = builder.build()
import ssl

ctx = ssl.create_default_context(cafile=r"cacert.pem")

get_requests_session(ctx)
