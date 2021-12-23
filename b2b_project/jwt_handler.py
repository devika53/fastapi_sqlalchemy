import time
import jwt


secret = 'de848c1c8a8de5afc65c88b12da0edda'
algorithm = 'HS256'

def token_response(token: str):
    return {
        "access token": token
    }

def signJWT(userID : str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600

    }
    token = jwt.encode(payload, secret,algorithm)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token,secret,algorithm)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return {}