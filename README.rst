sundog - SunSpec in Trio
========================

Resources
---------

=================================  =================================  =============================

`Documentation <documentation_>`_  `Read the Docs <documentation_>`_  |documentation badge|
`Issues <issues_>`_                `GitHub <issues_>`_                |issues badge|

`Repository <repository_>`_        `GitHub <repository_>`_            |repository badge|
`Tests <tests_>`_                  `GitHub Actions <tests_>`_         |tests badge|
`Coverage <coverage_>`_            `Codecov <coverage_>`_             |coverage badge|

`Distribution <distribution_>`_    `PyPI <distribution_>`_            | |version badge|
                                                                      | |python versions badge|
                                                                      | |python interpreters badge|

=================================  =================================  =============================


Introduction
------------

sundog provides asynchronous access to SunSpec devices using the `Trio`_ library.
The `SunSpec organization`_ has developed a device interface standard for the distributed energy industry.
The communication side of the standard is built as a layer on top of `Modbus`_.
SunSpec provides libraries including `pysunspec2`_ for loading the interface definition files and communicating with devices.
sundog uses pysunspec2 for the data handling and `pymodbus`_ for the communications.

.. _Trio: https://trio.readthedocs.io/
.. _SunSpec organization: https://sunspec.org/
.. _Modbus: https://en.wikipedia.org/wiki/Modbus
.. _pysunspec2: https://github.com/sunspec/pysunspec2
.. _pymodbus: https://pymodbus.readthedocs.io/


Installation
------------

This application is not yet published to PyPI nor built into directly runnable packages.
It is installable via either cloning and installing or directly via the Git repository.
When installing the Python package itself, it is recommended to work in a virtual environment.
For a quick introduction, see `Python Virtual Environments in Five Minutes <virtual_environments_>`_.

.. tab:: Unix/macOS

    .. code-block:: console

        $ myvenv/bin/pip install git+https://github.com/altendky/sundog

.. tab:: Windows

    .. code-block:: console

        $ myvenv/scripts/pip install git+https://github.com/altendky/sundog

.. _virtual_environments: https://chriswarrick.com/blog/2018/09/04/python-virtual-environments/


The Name
--------

`Sun dogs <wikipedia_general_>`_ are a pair of bright spots to either side of the sun created by the refraction of sunlight through ice crystals in the atmosphere.
The usage of dog in this case is `that of a verb meaning to hunt, track, or follow <wikipedia_etymology_>`_.
The two false suns will follow, or dog, the true sun through the sky.
With the two false suns following the one true sun we have a trio of suns.
Thus, here we are with the sundog library implementing SunSpec using Trio.

.. _wikipedia_general: https://en.wikipedia.org/wiki/Sun_dog
.. _wikipedia_etymology: https://en.wikipedia.org/wiki/Sun_dog#Etymology


.. _documentation: https://sundog.readthedocs.io
.. |documentation badge| image:: https://img.shields.io/badge/docs-read%20now-blue.svg?color=royalblue&logo=Read-the-Docs&logoColor=whitesmoke
   :target: `documentation`_
   :alt: Documentation

.. _distribution: https://pypi.org/project/sundog
.. |version badge| image:: https://img.shields.io/pypi/v/sundog.svg?color=indianred&logo=PyPI&logoColor=whitesmoke
   :target: `distribution`_
   :alt: Latest distribution version

.. |python versions badge| image:: https://img.shields.io/pypi/pyversions/sundog.svg?color=indianred&logo=PyPI&logoColor=whitesmoke
   :alt: Supported Python versions
   :target: `distribution`_

.. |python interpreters badge| image:: https://img.shields.io/pypi/implementation/sundog.svg?color=indianred&logo=PyPI&logoColor=whitesmoke
   :alt: Supported Python interpreters
   :target: `distribution`_

.. _issues: https://github.com/altendky/sundog/issues
.. |issues badge| image:: https://img.shields.io/github/issues/altendky/sundog?color=royalblue&logo=GitHub&logoColor=whitesmoke
   :target: `issues`_
   :alt: Issues

.. _repository: https://github.com/altendky/sundog
.. |repository badge| image:: https://img.shields.io/github/last-commit/altendky/sundog.svg?color=seagreen&logo=GitHub&logoColor=whitesmoke
   :target: `repository`_
   :alt: Repository

.. _tests: https://github.com/altendky/sundog/actions?query=branch%3Amain
.. |tests badge| image:: https://img.shields.io/github/workflow/status/altendky/sundog/CI/main?color=seagreen&logo=GitHub-Actions&logoColor=whitesmoke
   :target: `tests`_
   :alt: Tests

.. _coverage: https://codecov.io/gh/altendky/sundog
.. |coverage badge| image:: https://img.shields.io/codecov/c/github/altendky/sundog/main?color=seagreen&logo=Codecov&logoColor=whitesmoke
   :target: `coverage`_
   :alt: Test coverage
