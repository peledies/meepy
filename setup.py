import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meepy",
    version="0.0.3",
    author="Deac Karns",
    author_email="deac@hashsalt.net",
    description="A diagnostics package for when print statemets are not adequate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peledies/meepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
