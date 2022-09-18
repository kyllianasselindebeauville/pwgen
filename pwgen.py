import argparse
import secrets
import string


def generate_password(length: int = 16,
                      lowercase: bool = False,
                      uppercase: bool = False,
                      digits: bool = False,
                      symbols: bool = False) -> str:
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


def main():
    parser = argparse.ArgumentParser(description='Generate a password.')
    parser.add_argument('length', nargs='?', default=16, type=int,
                        help='length of the password to generate')
    parser.add_argument('-d', '--digits', action='store_true',
                        help='include digits in the password')
    parser.add_argument('-l', '--lowercase', action='store_true',
                        help='include lowercase letters in the password')
    parser.add_argument('-s', '--symbols', action='store_true',
                        help='include symbols in the password')
    parser.add_argument('-u', '--uppercase', action='store_true',
                        help='include uppercase letters in the password')

    args = parser.parse_args()
    password = generate_password(length=args.length, lowercase=args.lowercase,
                                 uppercase=args.uppercase, digits=args.digits,
                                 symbols=args.symbols)
    print(password)


if __name__ == '__main__':
    main()
