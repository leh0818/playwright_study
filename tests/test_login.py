from playwright.sync_api import expect

start_url = "https://vercel.com/signup"
def test_validation(page):
  page.goto(start_url)
  expect(page.get_by_role('button', name='Continue')).to_be_disabled() # 페이지 접근 시 버튼 활성화

  # page.get_by_text("I'm working on personal projects").click()
  page.get_by_test_id('signup-v2/hobby-select-option').click()
  page.get_by_label("Your Name").fill('abc')

  expect(page.get_by_role('button', name='Continue')).to_be_enabled() # 입력 시 버튼 활성화

