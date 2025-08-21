from .models import Token

def get_user_from_token(token_str):
    try:
        token_obj = Token.objects.get(key=token_str)
        return token_obj.user
    except Token.DoesNotExist:
        return None
