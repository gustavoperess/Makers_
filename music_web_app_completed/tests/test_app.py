
def test_get_all_albums(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    response = web_client.get("/albums")
    
    assert response.status_code == 200
    
    assert response.data.decode("utf-8") == "\n".join([
        "Music Library(1, Doolittle, 1989, 1)",
        "Music Library(2, Surfer Rosa, 1988, 2)",
        "Music Library(3, Waterloo, 1972, 3)",
        "Music Library(4, Bossanova, 1990, 1)",
        "Music Library(5, Lover, 2019, 1)"
    ])


"""
When: I make a POST request to /albums
I create a new album with title = Voyage , release_year=2022 , artist_id=2
Then: I should get a 200 with no content 
"""

def test_post_new_album(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    post_response = web_client.post("/albums", data={
                          "title": "Voyage",
                          "release_year": "2002",
                          "artist_id": "2"
    })
                          
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "\n".join([
        "Music Library(1, Doolittle, 1989, 1)",
        "Music Library(2, Surfer Rosa, 1988, 2)",
        "Music Library(3, Waterloo, 1972, 3)",
        "Music Library(4, Bossanova, 1990, 1)",
        "Music Library(5, Lover, 2019, 1)\n"
        "Music Library(6, Voyage, 2002, 2)"
    ])


"""
When: I make a GET request to /artists
I get a list with all artists in the repository
"""


def test_get_all_artists(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    response = web_client.get("/artists")
    
    assert response.status_code == 200
    
    assert response.data.decode("utf-8") == "\n".join([
                    "Artist(1, Pixies, Rock)",
                    "Artist(2, ABBA, Pop)",
                    "Artist(3, Taylor Swift, Pop)",
                    "Artist(4, Nina Simone, Jazz)"
    ])
 
"""
When: I make a Post request to /artists
I create a new artist with name = Wild Nothing, genre = Indie
Then I should get a 200 with no content
I should also make a get request to check if a new artist has been added
"""

def test_post_new_artist(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    post_response = web_client.post("/artists", data={
                          "name": "Wild nothing",
                          "genre": "Indie",
    })
                          
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "\n".join([
                    "Artist(1, Pixies, Rock)",
                    "Artist(2, ABBA, Pop)",
                    "Artist(3, Taylor Swift, Pop)",
                    "Artist(4, Nina Simone, Jazz)",
                    "Artist(5, Wild nothing, Indie)",
    ])
