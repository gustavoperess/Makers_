from playwright.sync_api import Page, expect




def test_create_new_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/")
    page.click("text = sign up")
    page.fill("input[name=title]", "Test Album")
    # page.fill("input[name=release_year]", "1998")
    # page.fill("input[name=artist_id]", "1")
    # page.click("text = add album")
    # title_element = page.locator(".t-title")
    # expect(title_element).to_have_text("Album: Test Album")
    # release_year_element = page.locator(".t-release_year")
    # expect(release_year_element).to_have_text("1998")