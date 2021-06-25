
nornir_pyxl
=============

A simple Open Pyxl plugin for `nornir <github.com/nornir-automation/nornir/>`_

Installation
------------

.. code::

    pip install nornir_pyxl

Example
-------
.. code::

    from nornir_pyxl.plugins.tasks import pyxl_ez_data
    from nornir import InitNornir

    nr = InitNornir("config.yml")


    def get_structured_data(task):
        """Get a list of dictionaries from Excel Spreadsheet with Nornir Pyxl."""
        data = pyxl_ez_data(task, workbook="example-workbook.xlsx", sheetname="IP_INFORMATION")

        # Loop through items and access dictionaries.
        for site_clli in data.result:
            print(site_clli["clli"])


    def main():
        """Execute Tasks."""
        nr.run(task=get_structured_data)

    if __name__ == "__main__"
        main()

Plugins
-------

Tasks
_____

* **pyxl_ez_data** - Loads an XLSX file and creates a list of dictionaries.
* **pyxl_map_data** - Loads an XLSX file and creates a list of dictionaries based on a user provided ENUM map.