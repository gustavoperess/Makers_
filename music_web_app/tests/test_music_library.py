from lib.music_library import MusicLibrary

"""
Music_libary constructs with an id, title and release_year
"""
def test_music_libary_constructs():
    music_libary = MusicLibrary(1, "Test Title", 2009)
    assert music_libary.id == 1
    assert music_libary.title == "Test Title"
    assert music_libary.release_year == 2009

"""
We can format books to strings nicely
"""
def test_music_libary_format_nicely():
    music_libary = MusicLibrary(1, "Test Title", 2009)
    assert str(music_libary) == "Music Libary(1, Test Title, 2009)"


"""
We can compare two identical albums
And have them be equal
"""
def test_books_are_equal():
    album1 = MusicLibrary(1, "Test Title", 2009)
    album2 = MusicLibrary(1, "Test Title", 2009)
    assert album1 == album2

