import secrets
import string


def generate_password(length: int = 16,
                      lowercase: bool = False,
                      uppercase: bool = False,
                      digits: bool = False,
                      symbols: bool = False,
                      **kwargs: bool) -> str:
    """Generates a password.

    Generates a secure random password using the secrets module.

    Args:
        length: Length of the password to generate.
        lowercase: Whether or not to include lowercase letters in the password.
        uppercase: Whether or not to include uppercase letters in the password.
        digits: Whether or not to include digits in the password.
        symbols: Whether or not to include symbols in the password.

    Returns:
        The generated password as a str.
    """
    characters = ((string.ascii_lowercase if lowercase else '') +
                  (string.ascii_uppercase if uppercase else '') +
                  (string.digits if digits else '') +
                  (string.punctuation if symbols else '') or
                  (string.ascii_letters + string.digits + string.punctuation))

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


generate = generate_password
