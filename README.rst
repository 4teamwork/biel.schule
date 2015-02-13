biel.schule
================

``biel.schule`` installation package to install biel.schule website

.. contents:: Table of Contents

Installation local development-environment
------------------------------------------

.. code:: bash

    $ git clone git@github.com:4teamwork/biel.schule.git
    $ cd biel.schule
    $ ln -s development.cfg buildout.cfg
    $ python2.7 bootstrap.py
    $ bin/buildout
    $ bin/instance fg

Dev-Test-Release-Process
------------------------

If you want to develop features, you must follow this guide

First checkout the package and create a new branch from the master:

.. code:: bash

    $ git clone git@github.com:4teamwork/biel.schule.git
    $ cd biel.schule
    $ git checkout -b my-mew-feature
    $ git push origin -u my-new-feature

If you are finnished and the feature is working fine,you can merge it into the
master branch after the quality-check:

.. code:: bash

    $ git checkout master
    $ git merge my-mew-feature
    $ git push

Now, the feature is available for other developers.

To provide the feature on the test-env or the prod-env, you can push the master
into the 'test' or 'production' branch.

.. code:: bash

    $ git push origin master:test
    $ git push origin master:production

Et voila, the feature is published.

Compatibility
-------------

Runs with `Plone <http://www.plone.org/>`_ `4.3`.


Links
-----

- Main github project repository: https://github.com/4teamwork/biel.schule
- Issue tracker: https://github.com/4teamwork/biel.schule/issues
- Continuous integration: https://jenkins.4teamwork.ch/search?q=biel.schule

Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``biel.schule`` is licensed under GNU General Public License, version 2.

