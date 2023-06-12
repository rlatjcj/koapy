from setuptools import setup, find_packages

setup(
    name="koapy",
    version="0.9.0",
    description="Kiwoom Open Api Plus Python",
    author="Yunseong Hwang",
    author_email="kika1492@gmail.com",
    url="https://github.com/elbakramer/koapy",
    packages=find_packages(include=["koapy"]),
    install_requires=["requirements.txt"],
)
