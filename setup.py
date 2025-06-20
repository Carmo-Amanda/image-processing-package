from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "image-processing_dio_amanda",
    version = "0.0.1",
    author = "Carmo-Amanda",
    author_email = "aaocarmo@gmail.com",
    description = "Image processing package",
    long_description = page_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Carmo-Amanda/image-processing-package.git",
    packages=find_packages(),
    install_requirements = requirements,
    python_requires='>=3.8',
)