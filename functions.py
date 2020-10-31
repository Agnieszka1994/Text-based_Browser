import os
import sys
from _collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore


def check_if_url(url):
    return '.' in url


def get_name_from_url(url):
    url = url.strip('https://')
    url = url.strip('http://')
    return url.split('.')[0]


def save_url_to_file(url, web_page, folder):
    file_name = get_name_from_url(url)
    with open(f"{folder}/{file_name}", "w") as file:
        print(web_page, file=file)


def get_page(url):
    if not url.startswith('https://'):
        url = 'https://' + url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = color_links_blue(soup)
    return soup.get_text()


def color_links_blue(soup):
    links = soup.find_all("a")
    for link in links:
        link.string = Fore.BLUE + link.text
    return soup


def print_url(url, folder):
    web_page = get_page(url)
    print(web_page)
    save_url_to_file(url, web_page, folder)


def print_from_file(url, folder):
    with open(f"{folder}/{url}") as bookmark:
        for line in bookmark:
            print(line)


def print_error():
    print('Error: Incorrect URL')


def main():
    # Catch the first argument from command line
    folder = sys.argv[1]
    # Create a folder
    os.makedirs(folder, exist_ok=True)
    # Create a stack for Last Recently Used
    LRU_cache = deque()

    while (request := input()) != 'exit':
        cached_pages = os.listdir(folder)
        if request == 'back' and LRU_cache:
            LRU_cache.pop()
            print_from_file(LRU_cache[-1], folder)
            continue
        elif request in cached_pages:
            print_from_file(request, folder)
            LRU_cache.append(request)
            continue
        elif check_if_url(request):
            print_url(request, folder)
            LRU_cache.append(get_name_from_url(request))
            continue
        print_error()
