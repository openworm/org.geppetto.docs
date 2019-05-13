from setuptools import setup, find_packages


setup(
    name='geppettodocs',
    version="1.0.0",
    license="MIT",
    description='Geppetto documentation',
    author='Geppetto contributors',
    author_email='info@geppetto.org',
    url='http://geppetto.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
