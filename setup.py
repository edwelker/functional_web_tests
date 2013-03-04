!#/usr/bin/env python
# vim:fileencoding=utf-8
from distutils.core import setup
from future import unicode_literals

requirements = [item for item in open('requirements.txt').read().splitlines()]

setup(
    name = "",
    version = "0.1.0",
    url = "",
    author = "Edward Welker",
    author_email = "eddie.welker@gmail.com",
    description = "A foundational selenium based web testing framework",
    license = "Public Domain",
    requirements = requirements,



)
