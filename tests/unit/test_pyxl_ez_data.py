#! /usr/bin/python3
"""Nornir Pyxl Ez Data UnitTests."""
from nornir_pyxl.plugins.tasks import pyxl_ez_data


def test_excel_file(nornir, get_success_ez_data, workbooks):
    """Testing valid excel file."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook=workbooks["working"],
        sheetname=workbooks["sheetname"],
    )
    assert data["test-nomad"][0].result[0] == get_success_ez_data


def test_wrong_sheetname(nornir, workbooks):
    """Attempt to open a spreadsheet that doesn't exist."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook=workbooks["broken"],
        sheetname=workbooks["sheetname"],
    )
    assert data["test-nomad"][0].failed
    assert str(data["test-nomad"][0].exception) == "IP_DATA does not exist."


def test_bad_workbook_success(nornir, get_success_ez_data_bad_wb, workbooks):
    """Load the poorly populated spreadsheet and generate only whats available."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook=workbooks["broken"],
        sheetname="SAR-Ax",
    )
    assert data["test-nomad"][0].result == get_success_ez_data_bad_wb


def test_wrong_filename(nornir):
    """Attempt to open a spreadsheet that doesn't exist."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook="I_dont_exist.xlsx",
        sheetname="no_worksheet",
    )
    assert data["test-nomad"][0].failed
    assert str(data["test-nomad"][0].exception) == "I_dont_exist.xlsx does not exist."


def test_wrong_extension(nornir):
    """Attempt to open a spreadsheet that doesn't exist."""
    data = nornir.run(
        task=pyxl_ez_data,
        workbook="file.xxx",
        sheetname="no_worksheet",
    )
    assert data["test-nomad"][0].failed
    assert str(data["test-nomad"][0].exception) == "file.xxx must end with 'xlsx'."
