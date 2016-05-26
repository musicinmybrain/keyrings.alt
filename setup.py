#!/usr/bin/env python
# Generated by jaraco.develop 2.27.1
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []
needs_wheel = {'release', 'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

test_requirements = [
    'gdata',
    'python-keyczar',
    'fs>=0.5',
    'pycrypto',
]
"dependencies for running tests"

if sys.version_info >= (3, 0):
    # gdata doesn't currently install on Python 3. Omit it also.
    # http://code.google.com/p/gdata-python-client/issues/detail?id=229
    test_requirements.remove('gdata')

    # keyczar doesn't currently install on Python 3. Omit it also.
    # http://code.google.com/p/keyczar/issues/detail?id=125
    test_requirements.remove('python-keyczar')

setup_params = dict(
    name='keyrings.alt',
    use_scm_version=True,
    author="Jason R. Coombs",
    author_email="jaraco@jaraco.com",
    description="Alternate keyring implementations",
    long_description=long_description,
    url="https://github.com/jaraco/keyrings.alt",
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    namespace_packages=['keyrings'],
    install_requires=[
    ],
    extras_require={
    },
    setup_requires=[
        'setuptools_scm>=1.9',
    ] + pytest_runner + sphinx + wheel,
    tests_require=[
        'keyring[test]',
        'backports.unittest_mock',
    ] + test_requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'keyring.backends': [
            'file = keyrings.alt.file',
            'Gnome = keyrings.alt.Gnome',
            'Google = keyrings.alt.Google',
            'keyczar = keyrings.alt.keyczar',
            'kwallet = keyrings.alt.kwallet',
            'multi = keyrings.alt.multi',
            'pyfs = keyrings.alt.pyfs',
            'Windows (alt) = keyrings.alt.Windows',
        ],
    },
)
if __name__ == '__main__':
    setuptools.setup(**setup_params)
