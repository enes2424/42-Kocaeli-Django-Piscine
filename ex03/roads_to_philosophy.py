import sys, requests
from bs4 import BeautifulSoup


def get_wikipedia_page(search_term):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = f"https://en.wikipedia.org/wiki/Special:Search?search={requests.utils.quote(search_term)}"
    response = requests.get(url, headers=headers)

    return response


def extract_title(soup):
    title_elem = soup.find("h1", {"id": "firstHeading"})
    return title_elem.text.strip() if title_elem else None


def is_redirect_page(soup):
    redirect_elem = soup.find("div", {"class": "redirectMsg"})
    return redirect_elem is not None


def find_first_valid_link(soup):
    content = soup.find("div", {"id": "mw-content-text"})
    if not content:
        return None

    sections = content.find_all("section")
    target_area = sections[0] if sections else content

    for paragraph in target_area.find_all("p", recursive=True):
        if not paragraph.get_text(strip=True):
            continue
        if paragraph.find_parent("table"):
            continue

        first_node = None
        for node in paragraph.contents:
            if getattr(node, "name", None) is None:
                if str(node).strip():
                    first_node = node
                    break
                continue
            first_node = node
            break
        if first_node is not None and getattr(first_node, "name", None) in ("i", "em", "sup"):
            continue

        for link in paragraph.find_all("a", href=True):
            href = link.get("href", "")
            if not href or href.startswith("#"):
                continue

            if href.startswith("/wiki/"):
                target = href
            elif "wikipedia.org/wiki/" in href:
                idx = href.find("/wiki/")
                target = href[idx:]
            else:
                continue

            if not target or "/wiki/" not in target:
                continue

            classes = link.get("class") or []
            if any("disambig" in str(c).lower() for c in classes):
                continue

            if target.startswith("/wiki/Help:") or target.startswith("/wiki/Wikipedia:"):
                continue
            if target.startswith("/wiki/Special:") or target.startswith("/wiki/Talk:"):
                continue
            if target.startswith("/wiki/Category:"):
                continue
            if ":" in target and not target.startswith("/wiki/File:"):
                continue
            if link.find_parent(["i", "em", "sup"]):
                continue

            paragraph_text = paragraph.get_text(" ", strip=False)
            link_text = link.get_text(" ", strip=False)
            pos = paragraph_text.find(link_text)
            if pos != -1:
                before = paragraph_text[:pos]
                after = paragraph_text[pos + len(link_text) :]
                if before.count("(") > before.count(")") or after.count(")") > after.count("("):
                    continue

            return target.replace("/wiki/", "")

    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py <search_term>")
        sys.exit(1)

    start_term = sys.argv[1]
    current_term = start_term
    visited_pages = []

    while True:
        if current_term in visited_pages:
            print("It leads to an infinite loop !")
            break

        visited_pages.append(current_term)

        response = get_wikipedia_page(current_term)
        if not response or response.status_code != 200:
            print(
                f"Error: Failed to fetch page '{current_term}' (status code: {response.status_code if response else 'no response'})"
            )
            break

        soup = BeautifulSoup(response.content, "html.parser")

        title = extract_title(soup)
        if not title:
            print(f"Error: Could not extract title from page '{current_term}'")
            break

        if title == "Search results":
            print("It leads to a dead end !")
            break

        print(f"{title}")

        if is_redirect_page(soup):
            redirect_link = soup.find("div", {"class": "redirectMsg"}).find("a", href=True)
            if redirect_link:
                href = redirect_link.get("href", "")
                if href.startswith("/wiki/"):
                    current_term = href.replace("/wiki/", "")
                    continue
                if "wikipedia.org/wiki/" in href:
                    idx = href.find("/wiki/")
                    current_term = href[idx:].replace("/wiki/", "")
                    continue
            print(f"Error: Could not find redirect target for '{current_term}'")
            break

        if title.lower() == "philosophy":
            print(f"{len(visited_pages)} roads from {start_term} to philosophy !")
            break

        next_link = find_first_valid_link(soup)
        if not next_link:
            print("It leads to a dead end !")
            break

        current_term = next_link


if __name__ == "__main__":
    main()
