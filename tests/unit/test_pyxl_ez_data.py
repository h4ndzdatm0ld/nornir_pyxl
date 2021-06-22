# #! /usr/bin/python3
# import os, pytest

# from nornir import InitNornir
# from nornir_pyxl.plugins.tasks import pyxl_ez_data

# data_dir = f"{os.path.dirname(os.path.realpath(__file__))}/test_data"


# class Test(object):
#     def test_template_file(self, nr):
#         data = nr.run(
#             task=pyxl_ez_data,
#             workbook=f"{data_dir}/working_example_wb.xlsx",
#             sheetname="IP_DATA",
#         )

#         for host, resultlist in data.items():
#             for x in resultlist:
#                 value = x.result[0]
#                 assert value["SITE_ID"] == "Q345501"

#     def test_broken_template_file(self, nr):
#         data = nr.run(
#             task=pyxl_ez_data,
#             workbook=f"{data_dir}/working_example_wb.xlsx",
#             sheetname="IP_DATA",
#         )

#         for host, resultlist in data.items():
#             for x in resultlist:
#                 value = x.result[0]
#                 print(value.items())
#                 assert "192.168.125.1/32" not in value.values()
