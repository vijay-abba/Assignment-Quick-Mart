import hashlib
import hmac

def check_password_v2(stored_string, provided_password):
    try:
        salt_hex, hash_hex = stored_string.split(":")
        salt = bytes.fromhex(salt_hex)
        stored_hash = bytes.fromhex(hash_hex)

        new_hash = hashlib.pbkdf2_hmac(
            "sha256", provided_password.encode("utf-8"), salt, 100000
        )

        print(hmac.compare_digest(new_hash, stored_hash))
    except Exception:
        return False


# check_password_v2(
#     "82cdd17b89a0a85b650003d07591b253:5a11c81a8417b49fc0ddf32bdbac3bed9fd2aaa1928e04ba208c788273829d7a",
#     "12345",
# )
