import pyperclip

from pwgen.cli import parse_args
from pwgen.password import generate_password


def main():
    args = parse_args()
    password = generate_password(**vars(args))

    if args.clipboard:
        pyperclip.copy(password)

    if args.print or not args.clipboard:
        print(password)


if __name__ == '__main__':
    main()
