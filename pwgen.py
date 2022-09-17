import argparse
import secrets
import string


def generate_password(length: int = 16, lowercase: bool = False) -> str:
    """Generates a password.

    Generates a secure random password using the secrets module.

    Args:
        length: Length of the password to generate.
        lowercase: Whether or not to include lowercase letters in the password.

    Returns:
        The generated password as a str.
    """
    characters = ((string.ascii_lowercase if lowercase else '') or
                  (string.ascii_letters + string.digits + string.punctuation))
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(description='Generate a password.')
    parser.add_argument('length', nargs='?', default=16, type=int,
                        help='length of the password to generate')
    parser.add_argument('-l', '--lowercase', action='store_true',
                        help='include lowercase letters in the password')

    args = parser.parse_args()
    password = generate_password(length=args.length, lowercase=args.lowercase)
    print(password)


if __name__ == '__main__':
    main()
