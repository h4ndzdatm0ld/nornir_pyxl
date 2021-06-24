#! /usr/bin/python3
"""Nornir Pyxl Ez Data UnitTests."""
import os
from nornir_pyxl.plugins.tasks import pyxl_ez_data

data_dir = f"{os.path.dirname(os.path.realpath(__file__))}/test_data"

WORKING_WORKBOOK = f"{data_dir}/working_example_wb.xlsx"
BROKEN_WORKBOOK = f"{data_dir}/broken_example_wb.xlsx"
SHEETNAME = "IP_DATA"


def test_excel_file(nornir, get_success_ez_data):
    """Testing valid excel file."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook=WORKING_WORKBOOK,
        sheetname=SHEETNAME,
    )
    assert data["test-nomad"][0].result[0] == get_success_ez_data


def test_wrong_sheetname(nornir):
    """Attempt to open a spreadsheet that doesn't exist."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook=BROKEN_WORKBOOK,
        sheetname=SHEETNAME,
    )
    assert data["test-nomad"][0].failed
    assert str(data["test-nomad"][0].exception) == "IP_DATA does not exist."


def test_bad_workbook_success(nornir, get_success_ez_data_bad_wb):
    """Load the poorly populated spreadsheet and generate only whats available."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook=BROKEN_WORKBOOK,
        sheetname="SAR-Ax",
    )
    assert data["test-nomad"][0].result == get_success_ez_data_bad_wb


def test_wrong_filename(nornir):
    """Attempt to open a spreadsheet that doesn't exist."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook="I_dont_exist.xlsx",
        sheetname=SHEETNAME,
    )
    assert data["test-nomad"][0].failed
    assert str(data["test-nomad"][0].exception) == "I_dont_exist.xlsx does not exist."


def test_wrong_extension(nornir):
    """Attempt to open a spreadsheet that doesn't exist."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook="file.xxx",
        sheetname=SHEETNAME,
    )
    assert data["test-nomad"][0].failed
    assert str(data["test-nomad"][0].exception) == "file.xxx must end with 'xlsx'."
