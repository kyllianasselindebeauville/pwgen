import argparse

from pwgen.version import __version__


def parse_args():
    """Parses arguments from the command-line.

    Creates a parser, adds arguments to the parser, parses those arguments.

    Returns:
        An argparse.Namespace object containing the arguments as attributes.
    """
    parser = argparse.ArgumentParser(prog='pwgen',
                                     usage='%(prog)s [options] [length]',
                                     description='Generate a password.',
                                     add_help=False)

    parser.add_argument('length', nargs='?', default=16, type=int,
                        help='length of the password')
    parser.add_argument('-c', '--clipboard', action='store_true',
                        help='copy the password to the clipboard')
    parser.add_argument('-d', '--digits', action='store_true',
                        help='include digits')
    parser.add_argument('-h', '--help', action='help',
                        help='show this help message and exit')
    parser.add_argument('-l', '--lowercase', action='store_true',
                        help='include lowercase letters')
    parser.add_argument('-p', '--print', action='store_true',
                        help='print the password to the terminal')
    parser.add_argument('-s', '--symbols', action='store_true',
                        help='include symbols')
    parser.add_argument('-u', '--uppercase', action='store_true',
                        help='include uppercase letters')
    parser.add_argument('-V', '--version', action='version',
                        version=f'%(prog)s {__version__}')

    args = parser.parse_args()
    return args
