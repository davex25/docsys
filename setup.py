from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='DocSys',
      version=version,
      description="Simple document management scripts",
      long_description="""\
Scripts for use with a scanner, e.g. multiple document scan and convert to png, interleave pages for feeder scanner.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='document management ocr indexing',
      author='Dave Friberg',
      author_email='dfriberg23@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'PyTesser'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
