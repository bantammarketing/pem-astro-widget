from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import time
import sys
from datetime import datetime

def is_deal_valid(validity_string):
    """Check if a deal is still valid based on its expiration date."""
    if not validity_string:
        return True  # If no date, assume valid
    
    try:
        # Parse date range like "01/01/2026 to 01/31/2026" or "02/01/2026 to 02/28/2026"
        if " to " in validity_string:
            end_date_str = validity_string.split(" to ")[-1].strip()
            # Parse date in MM/DD/YYYY format
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y")
            # Check if end date is today or in the future
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            return end_date >= today
        else:
            # If no "to" found, try to parse as single date
            try:
                end_date = datetime.strptime(validity_string.strip(), "%m/%d/%Y")
                today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                return end_date >= today
            except:
                return True  # If can't parse, assume valid
    except Exception as e:
        # If parsing fails, assume valid to be safe
        print(f"Warning: Could not parse validity date '{validity_string}': {e}")
        return True

def scrape_astro_deals(url, output_json="deals.json"):
    BASE_URL = "https://secure.astroloyalty.com"
    options = Options()
    options.add_argument("--headless")  # No browser window
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)  # Wait for JS to load

    html = driver.page_source

    # Save the rendered HTML for debugging
    with open("page_rendered.html", "w") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")
    deals = []
    expired_count = 0

    for offer in soup.select(".offer_box"):
        img_tag = offer.select_one("img")
        if img_tag and img_tag.get("src"):
            image = urljoin(BASE_URL, img_tag["src"])
        else:
            image = ""
        brand = offer.select_one(".mfg_heading")
        brand = brand.get_text(strip=True) if brand else ""
        title = offer.select_one(".offer_title")
        title = title.get_text(strip=True) if title else ""
        validity = offer.find(string=lambda text: "Offer Valid:" in text)
        if validity:
            validity_span = validity.parent
            dates = validity_span.find_all("br")
            if dates and len(dates) > 0:
                date_range = dates[-1].next_sibling.strip() if dates[-1].next_sibling else ""
            else:
                date_range = ""
        else:
            date_range = ""
        
        # Only add deal if it's still valid
        if is_deal_valid(date_range):
            deals.append({
                "brand": brand,
                "title": title,
                "image": image,
                "validity": date_range
            })
        else:
            expired_count += 1

    print(f"Found {len(deals)} active deals, filtered out {expired_count} expired deals")

    with open(output_json, "w") as f:
        json.dump(deals, f, indent=2)

    print(f"Scraped and saved deals to {output_json}")
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python astro_selenium_scraper.py <astro_deals_url> [output_json]")
        sys.exit(1)
    url = sys.argv[1]
    output_json = sys.argv[2] if len(sys.argv) > 2 else "deals.json"
    scrape_astro_deals(url, output_json)