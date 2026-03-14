import requests
import configuration
import data


def create_new_user():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers
    )


def create_kit(auth_token, kit_body):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token

    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )