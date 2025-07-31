import requests

def fetch_product_details(query_text: str) -> dict:
    search_url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        "search_terms": query_text,
        "search_simple": 1,
        "action": "process",
        "json": 1,
    }
    try:
        res = requests.get(search_url, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()
        if data.get("products"):
            return data["products"][0]
        return {}
    except Exception:
        return {}