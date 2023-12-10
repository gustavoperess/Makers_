from lib.post_repository import PostRepository
from lib.post import Post

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/users.sql") 
    repository = PostRepository(db_connection) 

    post = repository.all() 

    assert post == [
        Post(1, "title01", "content01", 145, 1),
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),
    ]

def test_to_find_a_single_post(db_connection):
    db_connection.seed("seeds/users.sql")
    a_repository = PostRepository(db_connection)
    
    albums = a_repository.find_single_post(2)
    assert albums == Post(2, "title02", "content02", 245, 1)


def test_to_find_all_posts_by_user(db_connection):
    db_connection.seed("seeds/users.sql")
    a_repository = PostRepository(db_connection)
    
    albums = a_repository.find_all_posts_by_user(1)
    assert albums == [
        Post(1, 'title01', 'content01', 145, 1),
        Post(2, 'title02', 'content02', 245, 1)
        ]



def test_to_create(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = PostRepository(db_connection) 
    
    post = Post(4, "title04", "content04",55, 3)
    assert repository.create(post) == None
    assert repository.all() == [
        Post(1, "title01", "content01", 145, 1),
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),
        Post(4, "title04", "content04",55, 3)
        
    ]

def test_to_delete(db_connection):
    db_connection.seed("seeds/users.sql") 
    repository = PostRepository(db_connection) 
   
    assert repository.delete(1) == None
    assert repository.all() == [
        Post(2, "title02", "content02", 245, 1),
        Post(3, "title03", "content03", 45, 2),
    ]

# NEED TO COME BACK
# def test_to_update(db_connection):
#     db_connection.seed("seeds/users.sql")
#     repository = PostRepository(db_connection) 
    
#     post = repository.find(1)
#     post.id = 1
#     assert repository.update(post) == None
#     assert repository.all() == [
#         Post(1, "title01", "content01", 145, 1),
#         Post(2, "title02", "content02", 245, 1),
#         Post(3, "title03", "content03", 45, 2),     
#     ]