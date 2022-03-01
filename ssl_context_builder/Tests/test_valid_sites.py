"""
This tests suite tests RequestsSecureSession and SslContextBuilder against valid sites in badssl.com
"""

from ssl_context_builder.builder.builder import SslContextBuilder
from ssl_context_builder.http_impl.requests_wrapper.secure_session import RequestsSecureSession

def test_invalid_endpoint_ecc256_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://ecc256.badssl.com').status_code == 200


def test_invalid_endpoint_ecc384_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://ecc384.badssl.com').status_code == 200


def test_invalid_endpoint_extended_validation_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://extended-validation.badssl.com').status_code == 200


def test_invalid_endpoint_rsa2048_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://rsa2048.badssl.com').status_code == 200


def test_invalid_endpoint_rsa4096_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://rsa4096.badssl.com').status_code == 200


def test_invalid_endpoint_rsa8192_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://rsa8192.badssl.com').status_code == 200


def test_invalid_endpoint_sha256_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://sha256.badssl.com').status_code == 200


def test_invalid_endpoint_sha384_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://sha384.badssl.com').status_code == 200


def test_invalid_endpoint_sha512_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://sha512.badssl.com').status_code == 200


def test_invalid_endpoint_tls_v1_2_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://tls-v1-2.badssl.com').status_code == 200


def test_invalid_endpoint_cbc_badssl_com():
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        assert s.session.get('https://cbc.badssl.com').status_code == 200