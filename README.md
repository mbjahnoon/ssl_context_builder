# SSL Context Builder

Making a secure https request is not an easy task. http libraries often hide sensitive configurations
that affects the request behavior in functional and security manner.

**security misconfiguration** is the No.5 category in the [OWASP TOP 10](https://owasp.org/www-project-top-ten/).
Indicates that 90% of applications were tested for some form of misconfiguration

This Project goals are:
1. To show what's going under the hood of requests library and suggest a way to handle misconfiguration issues.
2. Demonstrate how can we control and configure our SSL in an understandable way.
3. Show how system rootCA's can be accessed by python.

## Certification level

![](https://img.shields.io/badge/Repository%20purpose-Education-brightgreen)

This repo is for **Educational purpose only!**. Any use of it internal in production environment is highly discouraged.

## SslContextBuilder:
SslContextBuilder is a builder class implement fluent interface design pattern.
It's create and configure ssl.SSLContext class.

## Usage example:

More usage example can be found at `dry_run_examples.py` file

### Examples

#### Creating highly configured ssl_context:
Example of configuring SslContext to use strong ciphers
```
builder = SslContextBuilder()
ssl_ctx = builder.use_tls_1_2_and_above() \
    .set_maximum_key_exchange_security_level() \
    .set_cipher_type("chacha", "aes") \
    .set_key_length(256) \
    .set_cipher_mode("gcm") \
    .build()
```

#### Creating ssl_context in macOS environment:
Example of reading the macOS trusted CAs, 
(This is not done in SslContext or any http lib such as `requests` and `urlib`)
```
builder = SslContextBuilder()
ssl_ctx = builder.use_tls_1_2_and_above() \
    .chek_hostname_and_common_name() \
    .use_mac_os_cert('user') \
    .use_mac_os_cert('system') \
    .use_mac_os_cert('root') \
    .build()
```

#### Using requests in a more secure way
Example of creating a secure `requests` session.
We do three things that are not trivial and not part of `requests` library
1. Configuring the connection to use TLS_1_2 and above
2. Loading OS trusted certificates
3. Disable trust_env variables which is set to true by default in requests lib

Look into `RequestsSecureSession` implementation for more details.
``` python
ctx = builder.use_tls_1_2_and_above().use_windows_certs("ROOT")
with RequestsSecureSession(ctx) as secure_session:
    print(secure_session.session.get("https://google.com"))
```

#### Using aiohttp
Example of configuring aiohttp ssl_context. aiohttp comes with a build in option to 
configure ssl_context and trust it certificates.
```

url = "https://google.com"
ctx = SslContextBuilder().use_tls_1_2_and_above().build()

async def invoke_request():
    async with ClientSession() as session:
        async with session.get(url, ssl_context=ctx) as resp:
            print(await resp.text())

asyncio.run(invoke_request())
```