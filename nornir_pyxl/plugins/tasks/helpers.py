"""Helper Functions."""
from openpyxl import load_workbook
import sys
from pathlib import Path


def _calculate_reset(sheet_obj):
    """Calculate and Reset the Sheet Dimensions.

    Args:
        sheet_obj (openpyxl.worksheet): Sheet Object

    Return:
        sheet (openpyxl.worksheet): Recalculated Sheet Object
    """
    # Calculate Dimensions
    try:
        sheet_obj.calculate_dimension()
    except ValueError:
        sheet_obj.calculate_dimension(force=True)
    # Reset Dimensions
    sheet_obj.reset_dimensions()
    # Recalculate Dimensions
    sheet_obj.calculate_dimension(force=True)

    return sheet_obj


def _check_file(file_name):
    """Check file_name exists based on input."""
    file_path = Path(file_name)

    if not file_name.endswith(".xlsx"):
        sys.exit(f"Error: {file_path} must end with 'xlsx'.")
    return file_path.exists()


def open_excel_wb(file_name, sheetname):
    """Load an Excel Workbook and convert to Yaml.

    Args:
        file_name (str): File Path to Excel Workbook
        sheetname (str): Sheet Name to load

    Returns:
        Sheetname (openpyxl.worksheet): Loaded OpenPyxl Sheet Object
    """
    # Check if file provided via '-f' exists.
    # If it doesn't, exit the program.
    if not _check_file(file_name):
        sys.exit(f"{file_name} does not exist.")
    # Load the workbook
    workbook = load_workbook(
        filename=file_name, read_only=True, keep_vba=False, data_only=True
    )
    # Ensure sheetname exists inside the WorkBook.
    if sheetname not in workbook.sheetnames:
        sys.exit(f"{sheetname} does not exist.")

    # openpyxl.worksheet._read_only.ReadOnlyWorksheet
    # Recalculate Dimensions
    return _calculate_reset(workbook[sheetname])
