import pyshorteners

def shorten_url(url: str) -> str:
    """Shorten a given URL using the TinyURL service."""
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

# Example usage
long_url = "https://www.bing.com/search?q=saree+images&aqs=edge.0.69i64i450l2.5009176520j0j1&FORM=ANSPA1&PC=HCTS"
short_url = shorten_url(long_url)
print(f"Shortened URL: {short_url}")


