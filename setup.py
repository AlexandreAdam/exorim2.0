import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
        name="exorim",
        version="0.0.1",
        author="Alexandre Adam",
        author_email="alexandre.adam@umontreal.ca",
        long_description=long_description,
        packages=setuptools.find_packages(),
        python_requires=">3.6"
        )
