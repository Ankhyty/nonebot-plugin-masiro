
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="nonebot-plugin-masiro",
    version="1.0.0",
    description="a nonebot2 plugin to help you auto sign on masiro.me and return some information to you",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["nonebot-plugin-masiro"],
    author="Ankhyty",
    author_email="ankhyty@gmail.com",
    url="https://github.com/Ankhyty/nonebot-plugin-masiro",
    install_requires = ["nonebot2>=2.0.0b2","nonebot-adapter-onebot>=2.0.0b1"],
    python_requires=">=3.8.10"
)