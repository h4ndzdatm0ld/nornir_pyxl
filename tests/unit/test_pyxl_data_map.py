#! /usr/bin/python3
"""Nornir Pyxl Data Map UnitTests."""
import os

from nornir_pyxl.plugins.tasks.pyxl_data_map import pyxl_data_map
from tests.conftest import (
    NestedDataMap,
    DataMap,
    DIR_PATH,
)  # Class fixtures not supported.

WORKING_WORKBOOK = f"{DIR_PATH}/unit/test_data/working_example_wb.xlsx"
SHEETNAME = "IP_DATA"

# If NORNIR_LOG set to True, the log won't be deleted in teardown.
nornir_logfile = os.environ.get("NORNIR_LOG", False)


class TestNornirDataMap:
    """Test Class for DataMap"""

    def teardown_class(self):
        """Teardown."""
        # Remove nornir_log
        if not nornir_logfile:
            nornir_log = f"{DIR_PATH}/nornir_test.log"
            if os.path.exists(nornir_log):
                os.remove(nornir_log)

    def test_nested_dict(self, nornir, nested_dict):
        """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
        data = nornir.run(
            task=pyxl_data_map,
            workbook=WORKING_WORKBOOK,
            sheetname=SHEETNAME,
            mapping=NestedDataMap,
            min_row=2,
        )
        assert data["test-nomad"][0].result == nested_dict

    def test_dict(self, nornir, list_of_dicts):
        """Test to ensure the nested key with position 0 is the name of the outer dictionary."""
        data = nornir.run(
            task=pyxl_data_map,
            workbook=WORKING_WORKBOOK,
            sheetname=SHEETNAME,
            mapping=DataMap,
            min_row=2,
        )
        assert data["test-nomad"][0].result == list_of_dicts
