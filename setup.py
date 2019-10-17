import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shlumpy",
    version="0.0.1",
    author="Dor Elias, Michael Zion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shlum/shlumpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
