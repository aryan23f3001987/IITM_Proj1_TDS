from playwright.sync_api import sync_playwright
import time

def scrape_tds_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://tds.s-anand.net/#/2025-01/", wait_until="networkidle")

        # Wait for content to load
        time.sleep(5)

        # Extract visible content
        content = page.content()  # raw HTML
        text = page.inner_text("body")  # clean readable text

        with open("tds_course_content.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("✅ TDS Course content saved to tds_course_content.txt")

        browser.close()

if __name__ == "__main__":
    scrape_tds_site()