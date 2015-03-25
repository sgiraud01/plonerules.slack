from setuptools import setup, find_packages
import os

version = '1.0.4'

setup(name='plonerules.slack',
      version=version,
      description="Post to a slack channel action for plone rules",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='slack plone rules',
      author='Steve Giraud',
      author_email='sgiraud01@gmail.com',
      url='https://github.com/sgiraud01/plonerules.slack/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonerules'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'slacker',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
