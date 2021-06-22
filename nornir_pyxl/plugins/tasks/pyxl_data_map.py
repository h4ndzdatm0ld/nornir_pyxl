from enum import Enum
from openpyxl import load_workbook
from nornir.core.task import Result, Task
import sys
from pathlib import Path
from nornir_pyxl.plugins.tasks.helpers import open_excel_wb


def pyxl_data_map(
    task: Task,
    mapping: Enum,
    workbook,
    sheetname,
    min_row: int = None,
    max_row: int = None,
    min_col: int = None,
    max_col: int = None,
):

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
            DICT_KEY = row[mapping.NESTED_DICT.value].value
            row_map[DICT_KEY] = {}

        for map in mapping:
            if "NESTED_DICT" in mapping.__members__:
                # Skip over nested_dict key
                if map.name == mapping.NESTED_DICT.name:
                    pass
                else:
                    row_map[DICT_KEY].update({map.name: row[map.value].value})
            else:
                row_map[map.name] = row[map.value].value
        row_data.append(row_map)
    data["data"] = row_data
    return Result(host=task.host, result=data["data"])
