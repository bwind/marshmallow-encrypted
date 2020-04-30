# marshmallow-encrypted

Encrypted field for use with Marshmallow.

## How does it work?

EncryptedField transparently encrypts its contents during dump and decrypts its contents during load. This is useful for storing sensitive data in databases and provides an extra layer of security because your encryption key doesn't sit with the encrypted data but lives in your code instead.

This field depends on pycryptodome and uses AES to encrypt and decrypt data.

## Installation

```bash
pip install marshmallow_encrypted
```

## Usage

To use the field, you'll need to have a secret key. Your secret key must be either 16, 24 or 32 characters long. You can provide `secret_key` as a keyword argument to EncryptedField's constructor, otherwise it will fallback to the MARSHMALLOW_ENCRYPTED_SECRET_KEY environment variable.

Then, declare it as a field in a schema:

```python
from marshmallow import Schema
from marshmallow_encrypted import EncryptedField


class UserSchema(Schema):
    password = EncryptedField(secret_key="145c185d94771f66")
```
