from distutils.core import setup

setup (
name='EC2Spot',
version='0.1.1',
author='Dinesh P. Weerapurage',
author_email='xydinesh@gmail.com',
packages=['ec2spot'],
scripts=['bin/fabfile.py'],
url='http://pypi.python.org/pypi/EC2Spot',
license='LICENSE.txt',
long_description=open('README.txt').read(),
install_requires=[
"boto == 2.6.0",
],
)
