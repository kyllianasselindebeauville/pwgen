import secrets
import string


def generate_password(length: int = 16) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password