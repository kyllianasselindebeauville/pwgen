import argparse

from pwgen.version import __version__


def parse_args():
    parser = argparse.ArgumentParser(prog='pwgen',
                                     description='Generate a password.',
                                     add_help=False)

    parser.add_argument('length', nargs='?', default=16, type=int,
                        help='length of the password to generate')
    parser.add_argument('-d', '--digits', action='store_true',
                        help='include digits in the password')
    parser.add_argument('-h', '--help', action='help',
                        help='show this help message and exit')
    parser.add_argument('-l', '--lowercase', action='store_true',
                        help='include lowercase letters in the password')
    parser.add_argument('-s', '--symbols', action='store_true',
                        help='include symbols in the password')
    parser.add_argument('-u', '--uppercase', action='store_true',
                        help='include uppercase letters in the password')
    parser.add_argument('-V', '--version', action='version',
                        version=f'%(prog)s {__version__}')

    args = parser.parse_args()
    return args
