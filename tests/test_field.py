import os

import pytest
from marshmallow_encrypted.field import EncryptedField


def test_no_secret_key():
    with pytest.raises(TypeError):
        EncryptedField()


def test_secret_key_from_env():
    secret_key = "y" * 16
    os.environ["MARSHMALLOW_ENCRYPTED_SECRET_KEY"] = secret_key
    assert EncryptedField()._secret_key == secret_key


def test_secret_key_init():
    secret_key = "z" * 16
    assert EncryptedField(secret_key=secret_key)._secret_key == secret_key


def test_serialize():
    secret_key = "z" * 16
    field = EncryptedField(secret_key=secret_key)
    serialized = field._serialize("foo", None, None)
    assert {"ciphertext", "tag", "nonce"} == set(serialized.keys())


def test_deserialize():
    secret_key = "z" * 16
    value = "foo"
    field = EncryptedField(secret_key=secret_key)
    serialized = field._serialize("foo", None, None)
    assert field._deserialize(serialized, None, None, None) == value
