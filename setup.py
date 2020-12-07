#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  This file is part of "Spawned" project
#
#  Author: Roman Gladyshev <remicollab@gmail.com>
#  License: GNU Lesser General Public License v3.0 or later
#
#  SPDX-License-Identifier: LGPL-3.0+
#  License text is available in the LICENSE file and online:
#  http://www.gnu.org/licenses/lgpl-3.0-standalone.html
#
#  Copyright (c) 2020 remico

import platform
from pathlib import Path

import setuptools


if 'linux' not in platform.system().lower():
    raise OSError('The package requires GNU Linux. Aborting installation...')


def long_description():
    return Path("README.md").read_text()


def version():
    return Path("spawned/VERSION").read_text()


# make the distribution platform dependent
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None


setuptools.setup(
    name="spawned",
    version=version(),
    author="remico",
    author_email="remicollab@gmail.com",
    description="A simple python module for dealing with sub-processes",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/remico/spawned",
    packages=setuptools.find_packages(exclude=['sndbx', 'test', 'tests']),
    package_data={'': ['VERSION']},
    py_modules=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
    ],
    python_requires='>=3.8',
    install_requires=['pexpect'],
    license='LGPLv3+',
    platforms=['POSIX'],
    cmdclass={'bdist_wheel': bdist_wheel},
)
