import Functions
import requests
def test_1():
    order_create=Functions.create_order()
    order_num=Functions.get_info()
    assert order_num.status_code == 200