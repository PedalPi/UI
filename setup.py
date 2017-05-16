from os import path
from setuptools import setup


def readme():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, 'README.rst'), encoding='UTF-8') as f:
        return f.read()

setup(
    name='PedalPi-UI',
    version='0.2.0',

    description='A simple physical controller for change and view the current pedalboard',
    #long_description=readme(),

    url='https://github.com/PedalPi/UI',

    author='Paulo Mateus Moura da Silva (SrMouraSilva)',
    author_email='mateus.moura@hotmail.com',
    maintainer='Paulo Mateus Moura da Silva (SrMouraSilva)',
    maintainer_email='mateus.moura@hotmail.com',

    license="Apache Software License v2",

    packages=[
        'ui/',
        'ui/pages',
        'ui/pages/current_pedalboard',
        'ui/pages/home',
    ],
    package_data={},
    install_requires=[],

    test_suite='test',
    test_requires=[],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Multimedia :: Sound/Audio',
        'Programming Language :: Python :: 3'
    ],
    keywords='pedal-pi mod-host lv2 audio plugins-manager',

    platforms='Linux',
)
