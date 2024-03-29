
# Open Pyxl Plugin for [Nornir](github.com/nornir-automation/nornir)

## Table of Contents

- [Open Pyxl Plugin for Nornir](#open-pyxl-plugin-for-nornir)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Plugins -> Tasks](#plugins---tasks)
  - [Examples](#examples)
    - [Pyxl Ez Data](#pyxl-ez-data)
    - [Example - Map Data with Nested Dict Magic Key](#example---map-data-with-nested-dict-magic-key)

## Installation

------------

```bash
pip install nornir_pyxl
```

## Plugins -> Tasks

------------

- **pyxl_ez_data** - Loads an XLSX file and creates a list of dictionaries. Excel file must be in a specific format. Headers(keys) and row values are standardized.
- **pyxl_map_data** - Loads an XLSX file and creates a list of dictionaries based on a user provided ENUM map. Allows user to specify row & column start & end. Also allows flexibility on how results are generated by using a magic key, "NESTED_DICT" inside the ENUM map.

## Examples

### Pyxl Ez Data

![Image](docs/images/xlsx-preview.png)

This task plugin is expecting you to modify the Excel Spreadsheet for best results and it's kind of perfect world scenario. The list of dictionaries will be generated starting from row 2, always. Each column header starting from position 0 (A1) will be assigned the KEY. The task will also attempt to standardize the keys by doing the following:

- Trimming White Space

- Replacing dashes with underscores

- Converting all letters to lowercase

- Replacing any whitespace with an underscore

For Values the following modifications happen:

- If value is a datetime object, returns as a str

- If value is a str, but actually a digit -> returns as int

- None or none are returned as False. Same goes for empty cells.

------------

```python
from nornir_pyxl.plugins.tasks import pyxl_ez_data
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir


WORKBOOK = "working_example_wb.xlsx"


nr = InitNornir("config.yml")


def get_mapped_data(task):
    """Get a list of dictionaries from Excel Spreadsheet with Nornir Pyxl."""
    res = task.run(task=pyxl_ez_data,
        workbook=WORKBOOK,
        sheetname="IP_DATA",
    )

def main():
    """Execute Tasks."""
    print_result(nr.run(task=get_mapped_data))


if __name__ == "__main__":
    main()
```

The following output is the result of the above tasks:

```bash
❯ python3 test_pyxl.py
get_mapped_data*****************************************************************
* r1-csr ** changed : False ****************************************************
vvvv get_mapped_data ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- pyxl_ez_data ** changed : False ------------------------------------------- INFO
[ { 'clli': 'PHNZAZ',
    'ntp_server_1_ip': '192.168.1.100',
    'ntp_server_2_ip': '192.168.1.102/32',
    'ntp_server_3_ip': '192.168.100.3',
    'ntp_server_4_ip': 'time.ntp.com',
    'site_id': 'Q345501',
    'system_name': 'PHNZAZ -635696-01'}]
^^^^ END get_mapped_data ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

### Example - Map Data with Nested Dict Magic Key

![Image](docs/images/xlsx-preview.png)

------------
The following example uses the magic ENUM key, "NESTED_DICT". If this key is found in the ENUM mapping, it will take the value represented by the ENUM Mapping result (some index in every row) and create a nested dictionary with the rest of the values from the ENUM mapping inside of it. The actual value of the ENUM, "NESTED_DICT" key will not be duplicated inside the dictionary for each row.

Below you can see that NESTED_DICT is assigned to '0'. This represents the "SITE_ID" column header in our example spreadsheet. Therefore, it will loop through each row and generate a list of nested dictionaries in the following manner:

```json
[{'Q345501': {'CLLI': 'PHNZAZ', 'SYSTEM_NAME': 'PHNZAZ -635696-01'}}]
```

Now, if you were to remove the "NESTED_DICT" magic ENUM mapping, the results for each row would look like this:

```json
[{'CLLI': 'PHNZAZ', 'SYSTEM_NAME': 'PHNZAZ -635696-01'}]
```

It's important to note, in our example below we tell Open Pyxl to start from "min_row", "2". Otherwise, the list will start generating the list of dictionaries from row 1, which are the headers. This allows you the flexibility to pin point areas of a spread sheet which matter to your workflow.

Available options for identifying sections of interest in a spreadsheet:

- min row

- max row

- min col

- max col

```python
from nornir_pyxl.plugins.tasks import pyxl_data_map
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir
from enum import Enum


class DataMap(Enum):
    """Enum Class Mapping Desired Cells Of Interest by Index within their respective row."""

    NESTED_DICT = 0
    CLLI = 1
    SYSTEM_NAME = 2


WORKBOOK = "working_example_wb.xlsx"


nr = InitNornir("config.yml")


def get_mapped_data(task):
    """Get a list of dictionaries from Excel Spreadsheet with Nornir Pyxl."""
    res = task.run(task=pyxl_data_map,
        workbook=WORKBOOK,
        sheetname="IP_DATA",
        mapping=DataMap,
        min_row=2
    )

def main():
    """Execute Tasks."""
    print_result(nr.run(task=get_mapped_data))


if __name__ == "__main__":
    main()
```

The following output is the result of the above tasks:

```bash
❯ python3 test_pyxl.py
get_mapped_data*****************************************************************
* r1-csr ** changed : False ****************************************************
vvvv get_mapped_data ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- pyxl_data_map ** changed : False ------------------------------------------ INFO
[{'Q345501': {'CLLI': 'PHNZAZ', 'SYSTEM_NAME': 'PHNZAZ -635696-01'}}]
^^^^ END get_mapped_data ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
