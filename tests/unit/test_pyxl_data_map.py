#! /usr/bin/python3
import os, pytest

from nornir import InitNornir
from nornir_pyxl.plugins.tasks.pyxl_data_map import pyxl_data_map
from tests.conftest import NestedDataMap

data_dir = f"{os.path.dirname(os.path.realpath(__file__))}/test_data"

WORKING_WORKBOOK = f"{data_dir}/working_example_wb.xlsx"
SHEETNAME = "IP_DATA"


class TestDataMap(object):
    """Testing Data Map Task."""

    NESTED = [{"Q345501": {"SYSTEM_NAME": "PHNZAZ -635696-01"}}]

    def test_nested_dict(self, nr):
        """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
        data = nr.run(
            task=pyxl_data_map,
            workbook=WORKING_WORKBOOK,
            sheetname=SHEETNAME,
            mapping=NestedDataMap,
            min_row=2,
        )
        print(data["test-nomad"][0])
        assert data["test-nomad"][0] == TestDataMap.NESTED
