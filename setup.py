import codecs
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        description = f.read()
        # Remove graphql specifiers to prevent rst failing to render on pypi
        return description.replace('.. code-block:: graphql', '.. code-block::')


setup(
    name="pyariable",
    version="0.2.0",
    description="Placeholder variables to aid in testing.",
    long_description=long_description(),
    url="https://github.com/willemt/pyariable",
    author="willemt",
    author_email="himself@willemthiart.com",
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="development",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=[],
    package_data={},
    data_files=[],
    entry_points={},
)
