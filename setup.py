"""
Moded - A modeful diagram editor
================================
Moded attempts to bring the power of modal editing to diagram software.
Once you've felt the power of vim, or emacs, you sometimes wish more 
software would focus on power users. Enable them to create, modify and 
navigate swiftly, without leaving home row.

Moded is focused on power users. The current state is a more of a proof
of concept to show that modal editing indeed does work for diagram creation.
"""

from moded import __version__
from setuptools import setuptools


setup(
    name = 'Moded',
    version = __version__,
    url = "https://github.com/MelleB/moded/",
    license = "GNU GPLv3",
    author = "Melle Boersma",
    author_email = "moded@melleboersma.nl",
    description = "A modeful diagram editor",
    long_description = __doc__,
    install_requires = [
        'toml==0.9.1',
        'kivy==1.9.1'
    ],
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Graphics :: Editors',
        'Topic :: Software Development :: Documentation'
    ]
)
