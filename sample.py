
def get_user(name):
    password = "admin123"
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    print("Fetching user:", name)
    return query
