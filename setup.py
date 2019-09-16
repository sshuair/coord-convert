#coding: --utf-8--
from setuptools import setup

# version
with open('coord_convert/__init__.py') as f:
    for line in f:
        if line.find('__version__') >= 0:
            version = line.split('=')[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            break

# install requirements
with open('requirements.txt') as f:
    requirements = [x.strip() for x in f.readlines()]

# readme
with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='coord-convert',
    version = version,
    description = u'china mars coordinate convertor.',
    long_description = readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: GIS'],
    keywords='coordinate vector china',
    author='sshuair',
    author_email='sshuair@gmail.com',
    url='https://github.com/sshuair/coord-convert',
    packages = ['coord_convert'],
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        coord_covert=coord_convert.coordconvert:convertor
    '''

)
