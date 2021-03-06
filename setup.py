from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in multibranch/__init__.py
from multibranch import __version__ as version

setup(
	name="multibranch",
	version=version,
	description="Multi Branch",
	author="Syed Malik Ali",
	author_email="syedmalikali@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
