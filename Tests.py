import Functions
import requests
def test_geting_order():
    order_create = Functions.create_order()
    track_number = order_create.json()['track']
    order_num = Functions.get_info(str(track_number))
    assert order_num.status_code == 200


    # Бельцевич Дмитрий, 17-ая когорта. Финальный проект, инженер по тестированию плюс

