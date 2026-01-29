from playwright.sync_api import expect
import allure

start_url = "https://m.blog.naver.com/yyh8087/224164030520"

def test_meatball_button_click(page):
  page.goto(start_url)

  with allure.step("미트볼 버튼 클릭"):
    page.get_by_role("button", name="본문 기타 기능").click()
    menu = page.locator("#_tools_layer")

    expect(menu.get_by_role("link", name="공유하기")).to_be_visible()

  with allure.step("공유하기 버튼 클릭"):
    menu.get_by_role("link", name="공유하기").click()
    modal = page.locator("#naver-splugin-wrap")
    expect(modal.get_by_text("공유하기")).to_be_visible()


# def test_share_button_click(page):

  
