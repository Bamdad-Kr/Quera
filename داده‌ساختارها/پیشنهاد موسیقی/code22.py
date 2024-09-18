all_users = {}
all_albums = {}

def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = [age, city, albums]

def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = [artist_name, genre, tracks]

def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    count = 0
    for album in all_users[username][2]:
        if all_albums[album][0] == artist_name:
            count += all_albums[album][2]
    return count

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    count = 0
    for album in all_users[username][2]:
        if all_albums[album][1] == genre:
            count += all_albums[album][2]
    return count    

def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    count = 0
    for user in all_users.values():
        if user[0] == age:
            for album in user[2]:
                if all_albums[album][0] == artist_name:
                    count += all_albums[album][2]
    return count

def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    count = 0
    for user in all_users.values():
        if user[0] == age:
            for album in user[2]:
                if all_albums[album][1] == genre:
                    count += all_albums[album][2]
    return count

def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    count = 0
    for user in all_users.values():
        if user[1] == city:
            for album in user[2]:
                if all_albums[album][0] == artist_name:
                    count += all_albums[album][2]
    return count

def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    count = 0
    for user in all_users.values():
        if user[1] == city:
            for album in user[2]:
                if all_albums[album][1] == genre:
                    count += all_albums[album][2]
    return count

# Sample Test Case

# Adding albums
add_album("Album1", "Artist1", "Rock", 10, all_users, all_albums)
add_album("Album2", "Artist2", "Pop", 8, all_users, all_albums)
add_album("Album3", "Artist1", "Rock", 12, all_users, all_albums)

# Adding users
add_user("User1", 25, "CityA", ["Album1", "Album2"], all_users, all_albums)
add_user("User2", 30, "CityB", ["Album2", "Album3"], all_users, all_albums)
add_user("User3", 25, "CityA", ["Album3"], all_users, all_albums)

# Query user artist
print(query_user_artist("User1", "Artist1", all_users, all_albums))  # Output: 10

# Query user genre
print(query_user_genre("User2", "Pop", all_users, all_albums))  # Output: 8

# Query age artist
print(query_age_artist(25, "Artist1", all_users, all_albums))  # Output: 22

# Query age genre
print(query_age_genre(30, "Pop", all_users, all_albums))  # Output: 8

# Query city artist
print(query_city_artist("CityA", "Artist1", all_users, all_albums))  # Output: 22

# Query city genre
print(query_city_genre("CityB", "Rock", all_users, all_albums))  # Output: 12
