from setuptools import setup

setup(
    name="marshmallow_encrypted",
    include_package_data=True,
    install_requires=["marshmallow"],
    py_modules=["marshmallow_encrypted"],
    author="Bas Wind",
    author_email="mailtobwind+me@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Encrypted field for use with marshmallow",
    keywords=["marshmallow"],
    license="MIT",
    long_description=open("README.md").read(),
    platforms="any",
    url="https://github.com/bwind/marshmallow_encrypted",
    version="0.1.0",
)
