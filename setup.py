# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    # distutils breaks in Python2 when passing unicode strings in for packages
    # below. It pains me to have to drop unicode_literals; maybe we'll be able
    # to figure out how to bring it back soon.
    #
    #unicode_literals,
)

from distutils.core import setup
from pip.req import parse_requirements

import nattraverso


def get_install_requirements():
    """Returns a requirement list based on the contents of requirements.txt.
    """
    return [str(r.req) for r in parse_requirements("requirements.txt")]

setup(
    name="nattraverso",
    version=nattraverso.__version__,
    description="A NAT Traversal library",
    license="LGPL",
    author="Raphael Slinckx, Chapman Shoop",
    author_email="raphael@slinckx.net, chapman.shoop@gmail.com",
    url="https://github.com/belovachap/nattraverso",
    packages=[
        "nattraverso",
        "nattraverso.pynupnp",
    ],
    data_files=[
        ("", [
            "README",
            "requirements.txt",
        ]),
    ],
    install_requires=get_install_requirements()
)
