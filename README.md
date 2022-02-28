# SSL Context Builder

SSLContext for humans!

## Certification level

![](https://img.shields.io/badge/Repository%20purpose-Education-brightgreen)

This repo is for **Educational purpose only!**. Any use of it internal in production environment
is highly discouraged.

## Usage example:
More usage example can be found at `dry_run_examples.py` file

### Examples
- Creating highly configured ssl_context:
```
builder = SslContextBuilder()
ssl_ctx = builder.use_tls_1_2_and_above() \
    .set_post_handshake_auth(True) \
    .set_maximum_key_exchange_security_level() \
    .disable_session_ticket() \
    .disable_renegotiation() \
    .set_cipher_type("chacha", "aes") \
    .set_key_length(256) \
    .set_cipher_mode("gcm") \
    .chek_hostname_and_common_name() \
    .use_mac_os_cert('user') \
    .use_mac_os_cert('system') \
    .build()
   ```
- Creating ssl_context in macOS environment

```
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
```