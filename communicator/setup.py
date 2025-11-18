from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="communicator",
    version="0.0.1",
    description="Education-focused messaging module for Frappe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DappoF",
    author_email="support@example.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["frappe>=14.0.0"],
)
