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
inst_reqs = [
    'click', 'tqdm', 'fiona'
]

# readme
with open('README.md') as f:
    readme = f.read()

setup(
    name='coord-convert',
    version = version,
    description = u'china mars coordinate convertor.',
    long_description = readme,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: GIS'],
    keywords='coordinate vector china',
    author='sshuair',
    author_email='sshuair@gmail.com',
    url='https://github.com/sshuair/coord-convert',
    packages = ['coord_convert'],
    install_requires=inst_reqs,
    entry_points='''
        [console_scripts]
        coord_covert=coord_convert.coordconvert:convertor
    '''

)
