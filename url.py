import hashlib
import base64
import datetime
import string
import random
import zlib

def shorten_url(url, mappings):
    """Shortens a URL, handling collisions."""
    salt = str(datetime.datetime.now().timestamp())
    salted_url = url + salt
    hashed_url = hashlib.sha256(salted_url.encode()).digest()
    short_url_base = base64.urlsafe_b64encode(hashed_url[:6]).decode().rstrip('=')
    short_url = short_url_base
    counter = 0
    while short_url in mappings and counter < 20:
        counter += 1
        short_url = short_url_base + str(counter)
    if short_url not in mappings:
        mappings[short_url] = url
        return short_url
    else:
        return None

def resolve_url(short_url, mappings):
    """Resolves a short URL to its original URL."""
    return mappings.get(short_url, "Invalid URL")

def get_input(prompt):
    """Gets user input."""
    return input(prompt)

def display_output(text):
    """Displays output."""
    print(text)

def main():
    """Main function."""
    url_mappings = {}
    while True:
        long_url = get_input("Enter a URL to shorten (or press Enter to quit): ")
        if not long_url:
            break
        short_url = shorten_url(long_url, url_mappings)
        if short_url:
            display_output(f"Shortened URL: {short_url}")
            resolved_url = resolve_url(short_url, url_mappings)
            display_output(f"Resolved URL: {resolved_url}")
        else:
            display_output("Failed to shorten URL after several attempts. Please try again.")

if __name__ == "__main__":
    main()
