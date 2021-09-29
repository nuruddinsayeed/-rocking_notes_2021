from rocking_notes import auth


def authenticate(username, password):
    # user = auth.get_user_model().get(username, None)
    # if user and password == user.password:
    #     return user
    if auth.authenticate(username, password):
        user_model = auth.get_user_model()
        return user_model.get(user_model.username == username)


def identity(payload):
    user_id = payload['identity']
    print(f"identity--------->{user_id}<----------")
    return auth.get_user_model().get(user_id, None)
