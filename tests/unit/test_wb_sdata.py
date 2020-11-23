
#! /usr/bin/python3
import os, pytest

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_pyxl.plugins.tasks import wb_sdata

data_dir = f"{os.path.dirname(os.path.realpath(__file__))}/test_data"

class Test(object):

    def test_template_file(self, nr):
        data = nr.run(task=wb_sdata, workbook=f'{data_dir}/working_example_wb.xlsx',
                        sheetname='IP_DATA')

        for host, resultlist in data.items():          
            for x in resultlist:
                value = x.result
                assert value[0]['SITE_ID'] == 'Q345501'
            
