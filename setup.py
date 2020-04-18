#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

import pyevr

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

requirements = ['Click>=7.0', 'python-dateutil>=2.8.1', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=5.3.0', ]

setup(
    author=pyevr.__author__,
    author_email=pyevr.__email__,
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python client for EVR",
    entry_points={
        'console_scripts': [
            'pyevr=pyevr.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + changelog,
    include_package_data=True,
    keywords='pyevr',
    name='pyevr',
    packages=find_packages(include=['pyevr', 'pyevr.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/thorgate/pyevr',
    version=pyevr.__version__,
    zip_safe=False,
)
