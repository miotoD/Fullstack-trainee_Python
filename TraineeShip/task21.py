# URL shortner python

# format: URL = {short_url : url}

import random
import string

urls = {}

def random_word_generator():
    url = input("Enter or paste the url:")

    characters = string.ascii_letters + string.digits
    
    shortened = random.sample(characters,4)
    
    shortened_url = ''.join(shortened)
    
    urls[shortened_url] = url
    
    print(f"Original URL:{url}")
    print(f"Shortened to: {shortened_url}")


def view_urls():
    print("------------- Your URLs---------------")
    print(urls)


while True:
    print("\nURL Shortener Menu:")
    print("1. Shorten a URL")
    print("2. View URls")
    print("3. Exit")
    
    user_input = input("Enter:")
    
    if(user_input == "1"):
        random_word_generator()
        # break
    if(user_input == "2"):
        view_urls()
        # break
    if(user_input == "3"):
        break


