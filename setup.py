from setuptools import setup, find_packages
from package import LIBRARY_NAME

VERSION = "0.2"

f = open("README.md", 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name=LIBRARY_NAME,
    version=VERSION,
    description="Zegu - basic abstraction unit or mental model for developing microservices",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Przemysław Kot',
    author_email='przemyslaw.kot@gmail.com',
    url='https://github.com/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    # package_data={'simple': ['templates/*']},
    # include_package_data=True,
    entry_points="""
        [console_scripts]
    """
)
