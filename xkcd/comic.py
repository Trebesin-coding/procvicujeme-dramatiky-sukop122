from playwright.sync_api import sync_playwright

def main():

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://xkcd.com/")

        comic = page.locator('#comic img')
        comic.screenshot()

        print("Screenshot latest comic bummm")

        for i in range(3):
            comic = page.locator('#comic img')
            comic.screenshot(path=f'comic_{i+1}.png')

            print(f"Screenshot comic{i+1} bum bum")

            page.click('a[rel="next"]')
            page.wait_for_timeout(1000)

        page.wait_for_timeout(5000)
        browser.close()
        

if __name__ == "__main__":
    main()