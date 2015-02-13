from setuptools import setup, find_packages
import os

version = '1.0.0.dev0'


tests_require = [
    'plone.app.testing',
    'ftw.builder',
    'ftw.testing',
    'ftw.testbrowser',
]


setup(name='biel.schule',
      version=version,
      description="Policy for biel schulen.",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='',
      author='4teamwork',
      author_email='info@4teamwork.ch',
      url='http://www.4teamwork.ch',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['biel'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'setuptools',
          'ftw.inflator',
          'eGov',
          'plonetheme.onegov',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
