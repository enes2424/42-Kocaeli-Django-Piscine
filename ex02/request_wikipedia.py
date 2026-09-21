import requests, json, sys, dewiki


def fetch_page_by_title(title):
    base_api = "https://en.wikipedia.org/w/api.php"
    headers = {"User-Agent": "Wikipedia-API-Client/1.0 (https://example.com; contact@example.com)"}
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
        "titles": title,
        "redirects": 1,
    }
    try:
        resp = requests.get(base_api, params=params, headers=headers)
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    if resp.status_code != 200:
        print(f"Error: Received status code {resp.status_code}")
        sys.exit(1)

    try:
        return resp.json()
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response - {e}")
        sys.exit(1)


def extract_content_from_query(data):
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        return None
    page = next(iter(pages.values()))
    if page.get("missing") is not None or "revisions" not in page:
        return None
    return page["revisions"][0].get("*")


def write_to_file(search_term, content):
    try:
        plain_text = dewiki.from_string(content).strip()
    except Exception as e:
        print(f"Error: Failed to convert wiki markup to plain text - {e}")
        sys.exit(1)

    safe_name = search_term.replace(" ", "_")
    try:
        with open(f"{safe_name}.wiki", "w", encoding="utf-8") as f:
            f.write(plain_text)
    except OSError as e:
        print(f"Error: Failed to write file - {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py <search_term>")
        sys.exit(1)

    search_term = sys.argv[1]

    data = fetch_page_by_title(search_term)
    content = extract_content_from_query(data)

    if content is None:
        print("Error: No information found for the given query.")
        sys.exit(1)

    write_to_file(search_term, content)


if __name__ == "__main__":
    main()
