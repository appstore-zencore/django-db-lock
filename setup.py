import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
]

setup(
    name="django-db-lock",
    version="0.1.1",
    description="Lock something and keep status in database.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/django-db-lock",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['django-db-lock'],
    requires=requires,
    install_requires=requires,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=['django_db_lock'],
)