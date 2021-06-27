#! /usr/bin/python3
"""Nornir Pyxl Data Map UnitTests."""
from nornir_pyxl.plugins.tasks.pyxl_data_map import pyxl_data_map
from tests.conftest import (
    NestedDataMap,
    DataMap,
)  # Class fixtures not supported.


class TestNornirDataMap:
    """Test Class for DataMap"""

    def test_nested_dict(self, nornir, nested_dict, workbooks):
        """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
        data = nornir.run(
            task=pyxl_data_map,
            workbook=workbooks["working"],
            sheetname=workbooks["sheetname"],
            mapping=NestedDataMap,
            min_row=2,
        )
        assert data["test-nomad"][0].result == nested_dict

    def test_dict(self, nornir, list_of_dicts, workbooks):
        """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
        data = nornir.run(
            task=pyxl_data_map,
            workbook=workbooks["working"],
            sheetname=workbooks["sheetname"],
            mapping=DataMap,
            min_row=2,
        )
        assert data["test-nomad"][0].result == list_of_dicts
