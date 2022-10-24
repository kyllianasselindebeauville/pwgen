from setuptools import setup

exec(open('pwgen/version.py').read())

setup(
    name='pwgen',
    version=__version__,
    description='Generate secure passwords',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kyllian Asselin de Beauville',
    author_email='kyllianasselindebeauville@gmail.com',
    url='https://github.com/kyllianasselindebeauville/pwgen',
    packages=['pwgen'],
    license='MIT',
    install_requires=[
        'pyperclip>=1.8.2',
    ],
    entry_points={
        'console_scripts': [
            'pwgen = pwgen.__main__:main',
        ],
    },
    python_requires='>=3.7',
)
