import hashlib
import os
import hmac
import json

class RegistrationForm:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.role = "staff"
        self.flow()

    def validate_username(self):
        length_username = len(self.username)
        spaces_count = self.username.count(" ")
        if length_username >= 4 and length_username <= 20 and spaces_count == 0:
            return True
        else:
            print(
                "The username must be 4–20 characters long and should not contain spaces."
            )
            return False

    def validate_password(self):
        length_password = len(self.password)
        upper_count = len(list(filter(lambda c: c.isupper(), self.password)))
        digits_count = len(list(filter(lambda i: i.isnumeric(), self.password)))

        if length_password > 8 and upper_count >= 1 and digits_count >= 1:
            return True
        else:
            print(
                "Password must contain at least 9 characters, including at least 1 uppercase letter and 1 digit."
            )
            return False

    def hash_password(self):
        salt = os.urandom(16)

        # Explicitly call the constructor# Ensure password is encoded to bytes
        dk = hashlib.pbkdf2_hmac("sha256", self.password.encode("utf-8"), salt, 100000)

        # If dk is None, it means your Python build has a broken hashlib/OpenSSL link
        if dk is None:
            raise RuntimeError(
                "Hashlib failed to generate a key. Check your OpenSSL installation."
            )

        return salt.hex() + ":" + dk.hex()

    def save_it(self, hash):
        file_name = f"{self.username}.txt"
        user_dict = {
            "Username": self.username,
            "Password": hash,
            "Role": "staff"
        }
        user_dict_json = json.dumps(user_dict)

        with open(file_name, "w") as f:
            f.write(user_dict_json)

        print("Registration successful!")

    def flow(self):
        if(self.validate_username() and self.validate_password()):
            hash = self.hash_password()
            self.save_it(hash)


r1 = RegistrationForm("vijaykrishna", "1Vijaykrishna")

# r1 = RegistrationForm("vij", "a")
# The username must be 4–20 characters long and should not contain spaces.

# r1 = RegistrationForm("vi ja", "a")
# The username must be 4–20 characters long and should not contain spaces.

# r1 = RegistrationForm("vija", "a")
# Password must contain at least 9 characters, including at least 1 uppercase letter and 1 digit.

#r1 = RegistrationForm("vija", "abccefghi")
# Password must contain at least 9 characters, including at least 1 uppercase letter and 1 digit.

# r1 = RegistrationForm("vija", "abccefghI")
# Password must contain at least 9 characters, including at least 1 uppercase letter and 1 digit.



# ---- 


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
