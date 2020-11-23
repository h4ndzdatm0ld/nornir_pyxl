
#! /usr/bin/python3
import os, pytest

from nornir_utils.plugins.functions import print_result
from nornir_pyxl.plugins.tasks import wb_sdata

data_dir = f"{os.path.dirname(os.path.realpath(__file__))}/test_data"

class Test(object):

    def test_template_file(self, nr):
        data = nr.run(task=wb_sdata, workbook=f'{data_dir}/working_example_wb.xlsx',
                        sheetname='IP_DATA')
        print(data)
        # assert data
        # for v in data.result:
        #     print(v)
            # assert v['SITE_ID'] == 'Q345501'
            
        # for h, r in result.items():
        #     assert h in r.result
        #     if h == "host3.group_2":
        #         assert "my_var: comes_from_all" in r.result
        #     if h == "host4.group_2":
        #         assert "my_var: comes_from_host4.group_2" in r.result

#     def test_template_file_error_broken_file(self, nr):
#         results = nr.run(template_file, template="broken.j2", path=data_dir)
#         processed = False
#         for result in results.values():
#             processed = True
#             assert isinstance(result.exception, TemplateSyntaxError)
#         assert processed
