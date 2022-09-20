from pwgen.cli import parse_args
from pwgen.password import generate_password


def main():
    args = parse_args()
    password = generate_password(length=args.length, lowercase=args.lowercase,
                                 uppercase=args.uppercase, digits=args.digits,
                                 symbols=args.symbols)
    print(password)


if __name__ == '__main__':
    main()
