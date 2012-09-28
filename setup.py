import bisheng

from distutils.core import setup


setup(
    name='bisheng',
    version=bisheng.__version__,
    description='Beautifies Chinese/Japanese/Korean text that mixes with English and others.',
    author='Chang-Hung Liang',
    author_email='eliang.cs@gmail.com',
    license='BSD',
    packages=['bisheng'],
)
