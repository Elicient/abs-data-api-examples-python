from setuptools import setup

setup(
   name='elicientdata',
   version='1.0',
   description='Python client to make access to the data API easier',
   author='Elicient, Inc.',
   author_email='hello@elicient.com',
   packages=['.'],  #same as name
   install_requires=['requests-oauthlib'], #external packages as dependencies
)