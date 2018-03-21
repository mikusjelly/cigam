﻿from setuptools import setup, find_packages


if __name__ == "__main__":

    setup(
        name="cigam",
        version="0.0.3",
        description=("magic"),
        keywords="file type, file magic",
        license="MIT",

        packages=find_packages(exclude=['files']),

        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Utilities",
        ],

        author="mikusjelly",
        author_email="mikusjelly@gmail.com",
        url="https://github.com/mikusjelly/cigam",

    )
