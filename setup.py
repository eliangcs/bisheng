import bisheng

from distutils.core import setup


setup(
    name='bisheng',
    version=bisheng.__version__,
    url='https://github.com/eliangcs/bisheng',
    description='Adds spaces between Chinese/Japanese/Korean and halfwidth characters.',
    long_description=open('README.rst').read(),
    author='Chang-Hung Liang',
    author_email='eliang.cs@gmail.com',
    license='BSD',
    packages=['bisheng'],
)
