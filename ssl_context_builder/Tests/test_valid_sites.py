"""
This tests suite tests RequestsSecureSession and SslContextBuilder against valid sites in badssl.com
"""
import requests

from ssl_context_builder.builder.builder import SslContextBuilder
from ssl_context_builder.http_impl.requests_wrapper.secure_session import RequestsSecureSession


def secure_session_func(url):
    ctx = SslContextBuilder().use_tls_1_2_and_above().build()
    with RequestsSecureSession(ctx) as s:
        return s.session.get(url).status_code


def requests_original_func(url):
    return requests.get(url).status_code


invoke_func = secure_session_func


def test_invalid_endpoint_ecc256_badssl_com():
    assert invoke_func('https://ecc256.badssl.com') == 200


def test_invalid_endpoint_ecc384_badssl_com():
    assert invoke_func('https://ecc384.badssl.com') == 200


def test_invalid_endpoint_extended_validation_badssl_com():
    assert invoke_func('https://extended-validation.badssl.com') == 200


def test_invalid_endpoint_rsa2048_badssl_com():
    assert invoke_func('https://rsa2048.badssl.com') == 200


def test_invalid_endpoint_rsa4096_badssl_com():
    assert invoke_func('https://rsa4096.badssl.com') == 200


def test_invalid_endpoint_rsa8192_badssl_com():
    assert invoke_func('https://rsa8192.badssl.com') == 200


def test_invalid_endpoint_sha256_badssl_com():
    assert invoke_func('https://sha256.badssl.com') == 200


def test_invalid_endpoint_sha384_badssl_com():
    assert invoke_func('https://sha384.badssl.com') == 200


def test_invalid_endpoint_sha512_badssl_com():
    assert invoke_func('https://sha512.badssl.com') == 200


def test_invalid_endpoint_tls_v1_2_badssl_com():
    assert invoke_func('https://tls-v1-2.badssl.com') == 200


def test_invalid_endpoint_cbc_badssl_com():
    assert invoke_func('https://cbc.badssl.com') == 200
