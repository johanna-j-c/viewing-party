# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if not (title and genre and rating):
        return None
    else:
        movie_dict["title"]= title
        movie_dict["genre"]= genre
        movie_dict["rating"]= rating
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data  

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0.0
    if not user_data["watched"]:
        return sum
    for movie in user_data["watched"]:
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    genre_frequency_dict = {}
    if not user_data["watched"]:
        return None
    for movie in user_data["watched"]:
        if not movie["genre"] in genre_frequency_dict.keys():
            genre_frequency_dict[movie["genre"]]= 1
        else:
            genre_frequency_dict[movie["genre"]] += 1
    
    most_watched_genre = max(genre_frequency_dict, key = genre_frequency_dict.get)
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friend_watched_list.append(friend_movie["title"])

    user_set = set(user_watched_list)
    friend_set = set(friend_watched_list)
    unique_set = user_set - friend_set

    unique_list = []
    for title in unique_set:
        for movie in user_data["watched"]:
            if title == movie["title"]:
                unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friend_watched_list.append(friend_movie["title"])

    user_set = set(user_watched_list)
    friend_set = set(friend_watched_list)
    unique_set = friend_set - user_set

    unique_list = []
    for title in unique_set:
        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                if title == friend_movie["title"] and not (friend_movie in unique_list):
                    unique_list.append(friend_movie)
    return unique_list  

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_unique = get_friends_unique_watched(user_data)
    user_subscription_list = user_data["subscriptions"]
    recommendation_list = []
    

    for friend_dict in friend_unique:
        if friend_dict["host"] in user_subscription_list:
            recommendation_list.append(friend_dict)
    return(recommendation_list)
            

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_most_watched_genre = get_most_watched_genre(user_data)
    friend_unique = get_friends_unique_watched(user_data)
    recommendation_list = []

    for friend_dict in friend_unique:
        if friend_dict["genre"] == user_most_watched_genre:
            recommendation_list.append(friend_dict)
    return recommendation_list

def get_rec_from_favorites(user_data):
    user_unique = get_unique_watched(user_data)
    recommendation_list = []

    for favorite in user_data["favorites"]:
        if favorite in user_unique:
            recommendation_list.append(favorite)
    return recommendation_list
