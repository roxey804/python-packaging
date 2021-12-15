from setuptools import setup


setup(
   name='days_to_bday',
   version='0.1.0',
   author='Roxy',
   author_email='roxy@example.com',
   packages=['days_to_bday', 'days_to_bday.test'],
   scripts=['bin/script1','bin/script2'], #Not sure what these are for?
   url='http://github.com/pelucid/adr_client',
   description='A package to fugre out how many days to your next birthday',
   long_description=open('README.txt').read(),
   install_requires=[
       'pytest',
       'pendulum',
   ],
)
