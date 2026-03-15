from storage import load_data, save_data

def get_user(user_id):
    users = load_data()
    return users.get(str(user_id))

def create_user(user_id, profile):
    users = load_data()
    users[str(user_id)] = profile
    save_data(users)

def delete_user(user_id):
    users = load_data()
    if str(user_id) in users:
        del users[str(user_id)]
    save_data(users)