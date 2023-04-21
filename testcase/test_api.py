# -*- coding: gbk -*-
import requests
import pytest
import allure
from common.requestsutils import requests_utils
from common.readexcel import ExcelUtils
import logging
import json


@allure.feature("post�������")
class TestApi:
    # ��ȡ�ļ�����
    file_path = "../resource/testfiles.xlsx"
    read_ex = ExcelUtils(file_path)
    re_data = read_ex.read_excel_data()

    @pytest.mark.parametrize("args", re_data, ids=["����1", "����2"])
    def test_post(self, args):
        print(f"����ʽ��{args['request_method']}")
        print(f"����ͷ��{args['request_header']}")
        print(f"����url:{args['url']}")
        print(f"���������{args['parameters']}")
        logging.info("test--------begin")
        test_res = requests_utils(method=args['request_method'], url=args['url'], params=args['parameters'], \
                                  headers=json.loads(args['request_header']))
        print(f"��Ӧ�����{test_res}")
        assert test_res.get('status') == json.loads(args['expect_data'])['status']


if __name__ == "__main__":
    pa = "../testcase/test_api.py"
    pytest.main(['-vs', pa])
