import jwt
import datetime

SECRET_KEY = 'my_secret_key'


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."


# Example usage:
if __name__ == "__main__":
    authenticated_user_id = 123

    jwt_token = generate_token(authenticated_user_id)
    print("Generated Token:", jwt_token)

    result = verify_token(jwt_token)
    if isinstance(result, dict):
        print("Token is valid. User ID:", result['user_id'])
    else:
        print("Token verification failed:", result)
