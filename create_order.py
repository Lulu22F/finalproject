# Терновская Людмила, когорта 8а— Финальный проект, инженер по тестированию плюс


import sender_stand_request
import data


def test_get_track_number_info():
    order_full = sender_stand_request.post_new_order(data.order_body)
    track = {"t": order_full.json()["track"]}
    response = sender_stand_request.post_new_order_track(track)
    assert response.status_code == 200
