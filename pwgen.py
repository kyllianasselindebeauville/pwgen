import secrets
import string


def generate_password(length: int = 16) -> str:
    """Generates a password.

    Generates a secure random password using the secrets module.

    Args:
        length: Length of the password to generate.

    Returns:
        The generated password as a str.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    print(generate_password())


if __name__ == '__main__':
    main()
