"""
This tests suite tests RequestsSecureSession and SslContextBuilder against vulnerable sites in badssl.com
"""
import pytest
import requests
from requests.exceptions import SSLError, ConnectionError

from ssl_context_builder.builder.builder import SslContextBuilder
from ssl_context_builder.http_impl.requests_wrapper.secure_session import RequestsSecureSession


def secure_session_func(url):
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        return s.session.get(url)


def requests_original_func(url):
    return requests.get(url)


invoke_func = secure_session_func


def test_invalid_endpoint_expired_badssl_com():
    url = 'https://expired.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_incomplete_chain_badssl_com():
    url = 'https://incomplete-chain.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_invalid_expected_sct_badssl_com():
    url = 'https://invalid-expected-sct.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_known_interception_badssl_com():
    url = 'https://known-interception.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_no_common_name_badssl_com():
    url = 'https://no-common-name.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_no_subject_badssl_com():
    url = 'https://no-subject.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_reversed_chain_badssl_com():
    url = 'https://reversed-chain.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_self_signed_badssl_com():
    url = 'https://self-signed.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_untrusted_root_badssl_com():
    url = 'https://untrusted-root.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_wrong_host_badssl_com():
    url = 'https://wrong.host.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_dh_composite_badssl_com():
    url = 'https://dh-composite.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_dh1024_badssl_com():
    url = 'https://dh1024.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_dh480_badssl_com():
    url = 'https://dh480.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_dh512_badssl_com():
    url = 'https://dh512.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_3des_badssl_com():
    url = 'https://3des.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_null_badssl_com():
    url = 'https://null.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_rc4_md5_badssl_com():
    url = 'https://rc4-md5.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_rc4_badssl_com():
    url = 'https://rc4.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_ssl_v2_badssl_com():
    url = 'https://ssl-v2.badssl.com'
    with pytest.raises(ConnectionError):
        invoke_func(url)


def test_invalid_endpoint_ssl_v3_badssl_com():
    url = 'https://ssl-v3.badssl.com'
    with pytest.raises(ConnectionError):
        invoke_func(url)


def test_invalid_endpoint_tls_v1_0_badssl_com():
    url = 'https://tls-v1-0.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_tls_v1_1_badssl_com():
    url = 'https://tls-v1-1.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)


def test_invalid_endpoint_static_rsa_badssl_com():
    url = 'https://static-rsa.badssl.com'
    with pytest.raises(SSLError):
        invoke_func(url)

# ===================================================================================
# HPKP, SCT and CRL requires communication to 3rd party servers and are not supported
# ===================================================================================

# def test_invalid_endpoint_no_sct_badssl_com():
#     ctx = SslContextBuilder().use_tls_1_2_and_above() \
#         .set_post_handshake_auth(True) \
#         .disable_session_ticket() \
#         .disable_renegotiation() \
#         .chek_hostname_and_common_name() \
#         .use_windows_os_cert('ROOT') \
#         .use_windows_os_cert('CA') \
#         .use_windows_os_cert('MY') \
#         .build()
#     with pytest.raises(SSLError):
#         with RequestsSecureSession(ctx) as s:
#             s.session.get('https://no-sct.badssl.com')


# def test_invalid_endpoint_pinning_test_badssl_com():
#     ctx = SslContextBuilder().use_tls_1_2_and_above() \
#         .set_post_handshake_auth(True) \
#         .disable_session_ticket() \
#         .disable_renegotiation() \
#         .chek_hostname_and_common_name() \
#         .use_windows_os_cert('ROOT') \
#         .use_windows_os_cert('CA') \
#         .use_windows_os_cert('MY') \
#         .build()
#     with pytest.raises(SSLError):
#         with RequestsSecureSession(ctx) as s:
#             s.session.get('https://pinning-test.badssl.com')
#
#
# def test_invalid_endpoint_revoked_badssl_com():
#     ctx = SslContextBuilder().use_tls_1_2_and_above() \
#         .set_post_handshake_auth(True) \
#         .disable_session_ticket() \
#         .disable_renegotiation() \
#         .chek_hostname_and_common_name() \
#         .use_windows_os_cert('ROOT') \
#         .use_windows_os_cert('CA') \
#         .use_windows_os_cert('MY') \
#         .build()
#     with pytest.raises(SSLError):
#         with RequestsSecureSession(ctx) as s:
#             s.session.get('https://revoked.badssl.com')
