"""Nornir Pyxl Data Map Loader."""
from enum import Enum
from nornir.core.task import Result, Task
from nornir_pyxl.plugins.tasks.helpers import open_excel_wb


# pylint: disable=too-many-arguments
def pyxl_data_map(
    task: Task,
    mapping: Enum,
    workbook: str = None,
    sheetname: str = None,
    min_row: int = None,
    max_row: int = None,
    min_col: int = None,
    max_col: int = None,
) -> Result:
    r"""Loads a specific sheet from a workbook(xlsx file).

    Creates a list of dictionaries using the first row as the keys.

    Arguments:
        task (Task): Task
        mapping (Enum): Enum Class
        workbook (str, optional): Full Path to Excel Workbook. Defaults to None.
        sheetname (str, optional): Spreadsheet Name. Defaults to None.
        min_row (int, optional): min_row. Defaults to None.
        max_row (int, optional): max_row. Defaults to None.
        min_col (int, optional): min_col. Defaults to None.
        max_col (int, optional): max_col. Defaults to None.

    Examples:
        nr.run(task=pyxl_map_data, workbookfile="example-wb.xlsx',
               sheetname='ip_data', mapping=DataMap, row_min=2)

    Returns:
        Result object with the following attributes set:
        * result (''list''): list of dictionaries with
        data from the specific worksheet within the workbook.

    Notes:
        read_only: This is hardcoded set to true, as we don't do any writing or
        editing of the file.
    """
    data = {}
    row_data = []
    row_map = {}

    # Load the workbook & sheet
    sheet_obj = open_excel_wb(file_name=workbook, sheetname=sheetname)
    for row in sheet_obj.iter_rows(
        min_row=min_row,
        max_row=max_row,
        min_col=min_col,
        max_col=max_col,
        values_only=False,
    ):
        if "NESTED_DICT" in mapping.__members__:
            dict_key = row[mapping.NESTED_DICT.value].value
            row_map[dict_key] = {}
        for enum_map in mapping:
            if "NESTED_DICT" in mapping.__members__:
                # Skip over nested_dict key
                if enum_map.name == mapping.NESTED_DICT.name:
                    pass
                else:
                    row_map[dict_key].update({enum_map.name: row[enum_map.value].value})
            else:
                row_map[enum_map.name] = row[enum_map.value].value
        row_data.append(row_map)
    data["data"] = row_data

    return Result(host=task.host, result=data["data"])
