from setuptools import setup
import os, codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.2.8'
DESCRIPTION = 'pSock is a socket / threading module that helps developers and students to approach Server-Client creation and much more.'

setup(
    name="pSock",
    version=VERSION,
    author="Andrea Vaccaro (ANDRVV)",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages= ["pSock_lib"],
    license= "MIT License",
    keywords=["python", "socket", "threading", "server", "client"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
    )
