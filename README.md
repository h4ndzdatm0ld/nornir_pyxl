
# Open Pyxl plugin for [Nornir](github.com/nornir-automation/nornir)

## Table of Contents

- [Open Pyxl plugin for Nornir](#open-pyxl-plugin-for-nornir)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Plugins -> Tasks](#plugins---tasks)
  - [Examples](#examples)
    - [Pyxl Ez Data](#pyxl-ez-data)
    - [Example - Map Data](#example---map-data)

## Installation

------------

```bash
pip install nornir_pyxl
```

## Plugins -> Tasks

------------

- **pyxl_ez_data** - Loads an XLSX file and creates a list of dictionaries. Excel file must be in a specific format.
- **pyxl_map_data** - Loads an XLSX file and creates a list of dictionaries based on a user provided ENUM map. Allows user to specify row & column start & end.

## Examples

### Pyxl Ez Data

------------

```python
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
```

### Example - Map Data

------------

```python
TODO: Add working example with enum map and row
```
