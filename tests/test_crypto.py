from marshmallow_encrypted.crypto import decrypt, encrypt


def test_crypto_round_trip():
    value = b"foo"
    key = "x" * 16
    ciphertext, tag, nonce = encrypt(value, key)
    assert decrypt(ciphertext, tag, nonce, key) == value
