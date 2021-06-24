#! /usr/bin/python3
"""Nornir Pyxl Data Map UnitTests."""
import os

from nornir_pyxl.plugins.tasks.pyxl_data_map import pyxl_data_map
from tests.conftest import NestedDataMap, DataMap  # Class fixtures not supported.

data_dir = f"{os.path.dirname(os.path.realpath(__file__))}/test_data"

WORKING_WORKBOOK = f"{data_dir}/working_example_wb.xlsx"
SHEETNAME = "IP_DATA"


def test_nested_dict(nornir, nested_dict):
    """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
    data = nornir.run(
        task=pyxl_data_map,
        workbook=WORKING_WORKBOOK,
        sheetname=SHEETNAME,
        mapping=NestedDataMap,
        min_row=2,
    )
    assert data["test-nomad"][0].result == nested_dict


def test_dict(nornir, list_of_dicts):
    """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
    data = nornir.run(
        task=pyxl_data_map,
        workbook=WORKING_WORKBOOK,
        sheetname=SHEETNAME,
        mapping=DataMap,
        min_row=2,
    )
    assert data["test-nomad"][0].result == list_of_dicts
