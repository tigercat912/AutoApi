# -*- coding: gbk -*-
import requests
import pytest
import allure
from common.requestsutils import requests_utils
from common.readexcel import ExcelUtils
import logging
import json


@allure.feature("post请求测试")
class TestApi:
    # 获取文件数据
    file_path = "../resource/testfiles.xlsx"
    read_ex = ExcelUtils(file_path)
    re_data = read_ex.read_excel_data()

    @pytest.mark.parametrize("args", re_data, ids=["用例1", "用例2"])
    def test_post(self, args):
        print(f"请求方式：{args['request_method']}")
        print(f"请求头：{args['request_header']}")
        print(f"请求url:{args['url']}")
        print(f"请求参数：{args['parameters']}")
        logging.info("test--------begin")
        test_res = requests_utils(method=args['request_method'], url=args['url'], params=args['parameters'], \
                                  headers=json.loads(args['request_header']))
        print(f"响应结果：{test_res}")
        assert test_res.get('status') == json.loads(args['expect_data'])['status']


if __name__ == "__main__":
    pa = "../testcase/test_api.py"
    pytest.main(['-vs', pa])
