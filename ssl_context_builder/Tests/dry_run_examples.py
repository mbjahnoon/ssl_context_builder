import asyncio

from aiohttp import ClientSession

from ssl_context_builder.builder.builder import SslContextBuilder
from ssl_context_builder.http_impl.requests_wrapper.secure_session import RequestsSecureSession


def create_strong_crypto_ctx():
    builder = SslContextBuilder()
    ssl_ctx = builder.use_tls_1_2_and_above() \
        .set_maximum_key_exchange_security_level() \
        .set_cipher_type("chacha", "aes") \
        .set_key_length(256) \
        .set_cipher_mode("gcm") \
        .build()


def create_macos_tls_ctx():
    builder = SslContextBuilder()
    ssl_ctx = builder.use_tls_1_2_and_above() \
        .set_post_handshake_auth(True) \
        .disable_session_ticket() \
        .disable_renegotiation() \
        .chek_hostname_and_common_name() \
        .use_mac_os_cert('user') \
        .use_mac_os_cert('system') \
        .use_mac_os_cert('root') \
        .build()
    return ssl_ctx


def create_windows_tls_ctx():
    builder = SslContextBuilder()
    ssl_ctx = builder.use_tls_1_2_and_above() \
        .set_post_handshake_auth(True) \
        .disable_session_ticket() \
        .disable_renegotiation() \
        .chek_hostname_and_common_name() \
        .use_windows_os_cert('ROOT') \
        .use_windows_os_cert('CA') \
        .use_windows_os_cert('MY') \
        .build()
    return ssl_ctx


def secure_requests_session():
    ctx = create_macos_tls_ctx()
    with RequestsSecureSession(ctx) as secure_session:
        print(secure_session.session.get("https://google.com"))


def secure_requests_session_with_no_managed_context():
    ctx = create_macos_tls_ctx()
    secure_session = RequestsSecureSession(ctx)
    print(secure_session.session.get("https://google.com"))


def aiohttp_get():
    url = "https://google.com"
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()

    async def invoke_request():
        async with ClientSession() as session:
            async with session.get(url, ssl_context=ctx) as resp:
                print(await resp.text())

    asyncio.run(invoke_request())

