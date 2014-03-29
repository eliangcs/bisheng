import bisheng

from distutils.core import setup


def parse_requirements(filename):
    with open(filename) as f:
        content = f.read()
    return filter(lambda x: x and not x.startswith('#'), content.splitlines())


setup(
    name='bisheng',
    version=bisheng.__version__,
    url='https://github.com/eliangcs/bisheng',
    description='A set of utility functions for processing Chinese text.',
    long_description=open('README.rst').read(),
    author='Chang-Hung Liang',
    author_email='eliang.cs@gmail.com',
    license='BSD',
    packages=['bisheng'],
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
