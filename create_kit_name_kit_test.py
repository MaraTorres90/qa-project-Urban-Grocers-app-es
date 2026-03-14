import sender_stand_request
import data


def get_auth_token():
    user_response = sender_stand_request.create_new_user()
    return user_response.json()["authToken"]


def positive_assert(kit_body):
    token = get_auth_token()
    response = sender_stand_request.create_kit(token, kit_body)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert(kit_body):
    token = get_auth_token()
    response = sender_stand_request.create_kit(token, kit_body)

    assert response.status_code == 400


def test_create_kit_1_char():
    kit_body = {"name": "a"}
    positive_assert(kit_body)


def test_create_kit_511_char():
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    positive_assert(kit_body)


def test_create_kit_empty_name():
    kit_body = {"name": ""}
    negative_assert(kit_body)


def test_create_kit_512_char():
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    negative_assert(kit_body)


def test_special_characters():
    kit_body = {"name": "\"№%@\","}
    positive_assert(kit_body)


def test_spaces_allowed():
    kit_body = {"name": " A Aaa "}
    positive_assert(kit_body)


def test_numbers_allowed():
    kit_body = {"name": "123"}
    positive_assert(kit_body)


def test_no_parameter():
    kit_body = {}
    negative_assert(kit_body)


def test_wrong_type():
    kit_body = {"name": 123}
    negative_assert(kit_body)