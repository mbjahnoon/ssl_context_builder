# SSL Context Builder

Usage example:

```

if __name__ == '__main__':
    builder = SslContextBuilder()
    ssl_ctx = builder.use_tls_1_2_and_above() \
        .set_post_handshake_auth(True) \
        .set_maximum_key_exchange_security_level() \
        .configure_urllib_hardening() \
        .disable_renegotiation() \
        .set_cipher_type("chacha", "aes") \
        .set_key_length(256) \
        .set_cipher_mode("gcm") \
        .chek_hostname_and_common_name() \
        .use_mac_os_cert('user') \
        .use_mac_os_cert('system') \
        .build
   ```
