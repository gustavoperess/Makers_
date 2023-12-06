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