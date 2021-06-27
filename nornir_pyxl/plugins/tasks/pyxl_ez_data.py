"""Nornir Pyxl Ez Data Loader."""
from nornir.core.task import Result, Task
from nornir_pyxl.plugins.tasks.helpers import open_excel_wb
from .helpers import standardize


def pyxl_ez_data(
    task: Task,
    workbook: str,
    sheetname: str,
) -> Result:
    r"""Loads a specific sheet from a workbook(xlsx file).

    Creates a list of dictionaries using the first row as the keys.

    Arguments:
        workbook: Full path to .xlsx file
        sheetname: Worksheet Name

    Examples:
        nr.run(task=pyxl_ez_data, workbookfile="example-wb.xlsx',
               sheetname='ip_data')

    Returns:
        Result object with the following attributes set:
        * result (''list''): list of dictionaries with
        data from the specific worksheet within the workbook.

    Notes:
        read_only: This is hardcoded set to true, as we don't do any writing or
        editing of the file. This also allows the program to explicitly close
        the workbook object and avoid any I/O Operation errors being raised.
    """
    wsheet = open_excel_wb(workbook, sheetname)

    data_key = []
    for value in wsheet.iter_rows(values_only=True):
        for key in value:
            # Test adding 'or key.isspace():'
            if not key:
                pass
            else:
                data_key.append(standardize(key))
        break

    rows = []
    for rows_list in wsheet.iter_rows(values_only=True, min_row=2):
        row = []
        for values in rows_list:
            if not values:
                pass
            else:
                row.append(values)
        results = dict(zip(data_key, row))
        rows.append(results)

    # Filter out any potential empty dictionaries
    res = [row for row in rows if row]

    return Result(host=task.host, result=res)
