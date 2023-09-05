import requests
from config import api_key


def gif_search(api_key, q, limit=5) -> list | None:
    url = "https://api.giphy.com/v1/gifs/search"
    params = {"api_key": api_key, "q": q, "limit": limit}

    try:
        r = requests.get(url, params=params)
        data = r.json()

        gif_links = []

        for gif in data["data"]:
            gif_url = gif["images"]["original"]["url"]
            gif_links.append(gif_url)

        return gif_links

    except requests.exceptions.RequestException as ex:
        print(f"An error occurred while fetching data: {ex}")
        return None


def main() -> None:
    q = input("Please enter the keyword to search for GIFs: ")

    gif_links = gif_search(api_key, q)

    if gif_links:
        print("Found GIF links:")
        for link in gif_links:
            print(link)
    else:
        print("No GIF images found.")


if __name__ == "__main__":
    main()
