from setuptools import setup, find_packages

with open('README.md', "r", encoding="utf-8", newline="\n") as f:
    readme = f.read()

setup(
    name='lspython-full',
    version='0.1',
    description='An implementation of the "ls" command in Python',
    long_description=readme,
    url='https://github.com/Hanra-s-work/lspython-full',
    author="Henry Letellier",
    author_email='henry.letellier@gmail.com',
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'prettytable',
    ],
    entry_points={
        'console_scripts': [
            'lspython=lspython.lspython:lspython'
        ],
    },
    zip_safe=False
)
