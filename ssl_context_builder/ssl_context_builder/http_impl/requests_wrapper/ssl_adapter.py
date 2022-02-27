from requests.adapters import HTTPAdapter


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
