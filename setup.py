from setuptools import setup, find_packages
import os, codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'pSock is a socket / threading module that helps developers and students to approach Server-Client creation and much more.'

setup(
    name="pSock",
    version=VERSION,
    author="Andrea Vaccaro (ANDRVV)",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=["python", "socket", "threading", "server", "client"],
)
