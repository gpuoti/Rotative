#!/usr/bin/env python

from distutils.core import setup

setup(	name='rotative',
        version='0.1.2',
        description='Interface Sphinx documentation producer with Scons the build engine.',
        author='Giuseppe Puoti',
        author_email='giuseppe.puoti@gmail.com',
        url='',
        
        py_modules=[
            'rotative'
            # list them here when you add any other modules!
            ],
            
        
        
        install_requires = [
            'sphinx',
            'sphinx-rtd-theme'
            # add any other dependency package here in order to let pip install them as installation' side effect.
            ],
            
        scripts = []  
)