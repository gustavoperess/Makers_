from playwright.sync_api import Page, expect

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===


# def test_get_albums(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums.sql")
#     page.goto(f"http://{test_web_address}/albums")
#     div_tags = page.locator("div")
#     expect(div_tags).to_have_text(['\n       \n      title: Doolittle\n      Released: 1989\n       \n      title: Surfer Rosa\n      Released: 1988\n       \n      title: Waterloo\n      Released: 1972\n       \n      title: Bossanova\n      Released: 1990\n       \n      title: Lover\n      Released: 2019\n      \n    '])
    
    
def test_get_singe_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/details/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text([
        '\n Doolittle\n'
    ])
    expect(p_tag).to_have_text([
        'Release year:1989',
        'Artist: Pixies'
    ])

def test_show_single_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.wait_for_load_state("load")
    page.click('text=Doolittle')
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text('Album: Doolittle')
    expect(p_tag).to_have_text('1989')


def test_get_artist_only(page, test_web_address, db_connection):
     db_connection.seed("seeds/albums.sql")
     page.goto(f"http://{test_web_address}/artist/3")
     h1_tag = page.locator("h1")
     expect(h1_tag).to_have_text('Taylor Swift')
     page.click('text=Get all artist')
     a_tag = page.locator("(//h2/a)[1]")
     expect(a_tag).to_have_text("Pixies")


def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text = Add new album")
    page.fill("input[name=title]", "Test Album")
    page.fill("input[name=release_year]", "1998")
    page.fill("input[name=artist_id]", "1")
    page.click("text = add album")
    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Album: Test Album")
    release_year_element = page.locator(".t-release_year")
    expect(release_year_element).to_have_text("1998")



def test_attemp_creat_book_with_errors(page, test_web_address, db_connection):
     db_connection.seed("seeds/albums.sql")
     page.goto(f"http://{test_web_address}/albums")
     page.click("text = Add new album")
     page.click("text = add album")
     
     erros_tag = page.locator(".t-errors")
     expect(erros_tag).to_have_text("Your form contain erros: Title can't be blank, Release year can't be blank")
    


def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text = Add new artist")
    page.fill("input[name=name]", "Test Name")
    page.fill("input[name=genre]", "Rock")
    page.click("text = add artist")
    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("Test Name")
    release_year_element = page.locator(".t-genre")
    expect(release_year_element).to_have_text("Rock")


def test_attemp_creat_artist_with_errors(page, test_web_address, db_connection):
     db_connection.seed("seeds/albums.sql")
     page.goto(f"http://{test_web_address}/artists")
     page.click("text = Add new artist")
     page.click("text = add artist")
     
     erros_tag = page.locator(".t-errors")
     expect(erros_tag).to_have_text("Your form contain erros: Name can't be blank, Genre year can't be blank")
    
