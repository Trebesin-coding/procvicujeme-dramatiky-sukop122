from playwright.sync_api import sync_playwright
import os, json

path = os.path.join(os.path.dirname(__file__), "KniHovna.json")

def main():

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.databazeknih.cz")
        page.wait_for_timeout(2000)

        popularos = []

        popularanos = page.locator("div.book").all()

        for item in popularanos[:5]:
            title = item.locator(".title").inner_text()
            

            popularos.append({
                "title": title.strip(),
            })
            print(f"Popular bok : {title}")

        new_authoros = []

        new_bok = page.locator("div.newBooks div.book a").all()

        for i in range (min(3, len(new_bok))):
            new_bok[i].click()
            page.wait_for_timeout(2000)

            author = page.locator(".author a").inner_text()
            new_authoros.append(author.strip())

            print(f"New bok au thor: {author}")

            page.go_back()
            page.wait_for_timeout(2000)


        data = {
            "popular_books": popularos,
            "new_books": new_authoros
        }

        with open (path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    main()