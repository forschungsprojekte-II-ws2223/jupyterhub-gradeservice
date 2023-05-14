import time

import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["iat"] <= time.time() else None
    except TypeError:
        return {}
    except jwt.exceptions.InvalidSignatureError as err:
        print(str(err))
        return {}
