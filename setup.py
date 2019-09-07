from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ibdatastream",
    version="0.1.0",
    author="Justin Spahr-Summers",
    author_email="justin@jspahrsummers.com",
    description="Microservice to connect to Interactive Brokers and stream market data elsewhere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jspahrsummers/ibdatastream",
    packages=find_packages(),
    package_data={"ibdatastream": ["ibdatastream.proto", "py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    install_requires=["grpcio ~= 1.23", "ib-insync ~= 0.9.56", "protobuf ~= 3.9"],
    keywords="trading investing finance ib ibkr tws",
)
