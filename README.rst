
nornir_pyxl
=============

A simple Open Pyxl plugin for `nornir <github.com/nornir-automation/nornir/>`_

Installation
------------

.. code::

    pip install nornir_pyxl

Example
-------

from nornir_pyxl.plugins.tasks import pyxl_ez_data
from nornir import InitNornir

nr = InitNornir("config.yml")


def get_structured_data(task):

    data = pyxl_ez_data(task, workbook="example-workbook.xlsx", sheetname="IP_INFORMATION")

    for site_clli in data.result:
        print(site_clli["CLLI"])


def main():

    nr.run(task=get_structured_data)


main()

Plugins
-------

Tasks
_____

* **pyxl_ez_data** - Loads an XLSX file and creates a list of dictionaries.
