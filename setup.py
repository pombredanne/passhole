from setuptools import setup

setup(
    name='passhole',
    version='0.4.1',
    packages=['passhole'],
    author="Evan Widloski",
    author_email="evan@evanw.org",
    description="dmenu interface to KeePass databases",
    long_description=open('README.rst').read(),
    license="MIT",
    keywords="keepass dmenu password store passwords",
    url="https://github.com/purduelug/passhole",
    entry_points={
        'console_scripts': ['passhole = passhole.passhole:main']
    },
    install_requires=[
        "PyUserInput",
        "pykeepass",
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)