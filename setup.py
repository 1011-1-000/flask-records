# coding=utf-8
import os
import sys
from shutil import rmtree
from setuptools import setup, Command

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'flask-records.egg-info'))
        except FileNotFoundError:
            pass

        self.status('Building Source and Wheel (universal) distribution...')
        os.system('python setup.py sdist')

        self.status('Uploading the package to PyPi via Twine...')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name="flask_records",
    version="0.0.15",
    author="leo",
    author_email="leo.anonymous@qq.com",
    description="Flask wrapper for the SQL Records",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1011-1-000/flask-records",
    packages=['flask_records'],
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[
        'Flask>=0.9',
        'Flask-SQLAlchemy>=1.0',
        'records>=0.5.3',
        'pandas>=0.23.0'
    ],
    tests_require=[
        'Flask>=0.9',
        'Flask-SQLAlchemy>=1.0',
        'records>=0.5.3',
        'pandas>=0.23.0'
    ],
    cmdclass={
        'publish': PublishCommand,
    }
)
