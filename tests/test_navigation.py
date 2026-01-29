from playwright.sync_api import expect
import re

def test_Get_Started_Button(page):
    start_url = "https://nextjs.org/"
    h1 = "Next.js Docs"
    title = "Next.js Docs | Next.js"
    title_re = "Next.js"

    page.goto(start_url)
    page.get_by_role("link", name="Get Started").click()

    expect(page.get_by_role('heading', name=h1, level=1)).to_be_visible()
    expect(page).to_have_title (title)   
    expect(page).to_have_title(re.compile(title_re)) # 정규식
