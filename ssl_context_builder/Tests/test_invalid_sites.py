"""
This tests suite tests RequestsSecureSession and SslContextBuilder against vulnerable sites in badssl.com
"""
import pytest

from ssl_context_builder.builder.builder import SslContextBuilder
from ssl_context_builder.http_impl.requests_wrapper.secure_session import RequestsSecureSession


def test_invalid_endpoint_expired_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://expired.badssl.com')


def test_invalid_endpoint_incomplete_chain_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://incomplete-chain.badssl.com')


def test_invalid_endpoint_invalid_expected_sct_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://invalid-expected-sct.badssl.com')


def test_invalid_endpoint_known_interception_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://known-interception.badssl.com')


def test_invalid_endpoint_no_common_name_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://no-common-name.badssl.com')


def test_invalid_endpoint_no_subject_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://no-subject.badssl.com')


def test_invalid_endpoint_reversed_chain_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://reversed-chain.badssl.com')


def test_invalid_endpoint_self_signed_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://self-signed.badssl.com')


def test_invalid_endpoint_untrusted_root_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://untrusted-root.badssl.com')


def test_invalid_endpoint_wrong_host_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://wrong.host.badssl.com')


def test_invalid_endpoint_dh_composite_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://dh-composite.badssl.com')


def test_invalid_endpoint_dh1024_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://dh1024.badssl.com')


def test_invalid_endpoint_dh480_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://dh480.badssl.com')


def test_invalid_endpoint_dh512_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://dh512.badssl.com')


def test_invalid_endpoint_3des_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://3des.badssl.com')


def test_invalid_endpoint_null_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://null.badssl.com')


def test_invalid_endpoint_rc4_md5_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://rc4-md5.badssl.com')


def test_invalid_endpoint_rc4_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://rc4.badssl.com')


def test_invalid_endpoint_ssl_v2_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://ssl-v2.badssl.com')


def test_invalid_endpoint_ssl_v3_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://ssl-v3.badssl.com')


def test_invalid_endpoint_tls_v1_0_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://tls-v1-0.badssl.com')


def test_invalid_endpoint_tls_v1_1_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://tls-v1-1.badssl.com')


def test_invalid_endpoint_static_rsa_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with pytest.raises(Exception):
        with RequestsSecureSession(ctx) as s:
            s.session.get('https://static-rsa.badssl.com')

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
#     with pytest.raises(Exception):
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
#     with pytest.raises(Exception):
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
#     with pytest.raises(Exception):
#         with RequestsSecureSession(ctx) as s:
#             s.session.get('https://revoked.badssl.com')
