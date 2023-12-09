from playwright.sync_api import Page, expect


# def test_register_page(page, test_web_address, db_connection):
#     db_connection.seed("seeds/users.sql")
#     page.goto(f"http://{test_web_address}/")
#     page.click("text = sign up")
#     page.fill("input[name=username]", "UserName")
#     page.fill("input[name=password]", "12345678")
#     page.click("#submit")
#     page.screenshot(path="screenshot.png", full_page=True)
#     #print(page.content())
#     h1_tag = page.locator("h1")
#     expect(h1_tag).to_have_text('You are logged in')


def test_login_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name=username]", "Gustavo")
    page.fill("input[name=password]", "Gustavo123")
    page.click("#submit")
    page.screenshot(path="screenshot.png", full_page=True)
    print(page.content())
 