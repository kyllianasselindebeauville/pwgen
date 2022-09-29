# PwGen

PwGen is a secure password generator written in Python.

## Requirements

Make sure you have [Python 3.7+](https://www.python.org/downloads/) with [pip](https://pip.pypa.io/en/stable/installation/) installed.

```shell
python3 --version && python3 -m pip --version
```

## Installation

- Clone this repository.

```shell
git clone https://github.com/kyllianasselindebeauville/pwgen.git
```

- Change directory into it.

```shell
cd pwgen
```

- Use the package manager `pip` to install `pwgen`.

```shell
python3 -m pip install .
```

## Usage

```
usage: pwgen [options] [length]

Generate a password.

positional arguments:
  length           length of the password

options:
  -c, --clipboard  copy the password to the clipboard
  -d, --digits     include digits
  -h, --help       show this help message and exit
  -l, --lowercase  include lowercase letters
  -p, --print      print the password to the terminal
  -s, --symbols    include symbols
  -u, --uppercase  include uppercase letters
  -V, --version    show program's version number and exit
```

## Examples

- Generate an 8-character password including lowercase letters and digits.

```shell
pwgen -ld 8
```

- Generate a 16-character password including letters, digits and symbols *(default behavior)*.

```shell
pwgen
```

- Generate a 32-character password including uppercase letters and symbols.

```shell
pwgen -us 32
```

## Contributing

Pull requests are welcome. Please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)
