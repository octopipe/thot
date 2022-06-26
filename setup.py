from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
with open("README.md", "r") as f:
    README_TEXT = f.read()

setup(
    name = "thot",
    version = "0.0.1",
    author = "Maycon Pacheco",
    author_email = "mayconjrpacheco@gmail.com",
    description = "This package provides mechanisms for building a full text search engine",
    license = "MIT",
    keywords = ["full-text-search", "inverted-index", "tf", "idf", "search-engine"],
    url = "https://github.com/octopipe/thot",
    packages=find_packages(exclude=["build", ]),
    long_description=README_TEXT,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
