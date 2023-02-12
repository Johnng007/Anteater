#!/usr/bin/python3

import argparse
import requests
import random
import time
import socks
import socket
from bs4 import BeautifulSoup
from colorama import Fore, Style
import signal
from tqdm.auto import tqdm

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
 
signal.signal(signal.SIGINT, handler)

blue = Fore.BLUE
yellow = Fore.YELLOW
red = Fore.RED
magenta = Fore.MAGENTA
cyan = Fore.CYAN
DIM = Style.DIM
green = Fore.GREEN
RESET = Fore.RESET
BOLD = Style.BRIGHT
RESET_ALL = Style.RESET_ALL


print("\033[91m" 
            f"""
    Interesting Loot           Reconnaissance          
      / \   _ __ | |_ ___  __ _| |_ ___ _ __ 
     / _ \ | '_ \| __/ _ \/ _` | __/ _ \ '__|
    / ___ \| | | | ||  __/ (_| | ||  __/ |   
   /_/   \_\_| |_|\__\___|\__,_|\__\___|_|   
                coded by The El Pontiffico                             
        """,  
         "\033[0m" )

# Define the command line arguments
parser = argparse.ArgumentParser(description='Anteater Usage', formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=27))
parser.add_argument('url', help='URL of the website to be analyzed')
parser.add_argument('-p', '--proxy', help='Text file containing the proxy list to be used')
parser.add_argument('-d', '--delay', type=int, help='Time delay in minutes between each request')
parser.add_argument('-t', '--tor', action='store_true', help='Connect through Tor network')


# Parse the command line arguments
args = parser.parse_args()

# Read the proxy list from file
if args.proxy:
    with open(args.proxy, 'r') as f:
         #proxy_list = f.read().splitlines()
         proxy_list = f.readlines()
else:
    proxy_list = []


# Remove the newline characters from each proxy
proxy_list = [proxy.strip() for proxy in proxy_list]

#proxied = {random.choice(proxy_list)}




# Read the user agent list from file
with open('ANTS/ant_useragents.txt', 'r') as f:
    user_agents = f.read().splitlines()


def send_request(url, proxy=None):
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        if proxy:
            response = requests.get(url, headers=headers, proxies={"http": proxy_list, "https": proxy_list})
            #response = requests.get(url, headers=headers, proxies=proxy)
        else:
            response = requests.get(url, headers=headers)
        return response
    except:
        return None


def detect_cms_and_tech_stack(url, proxy=None):
    response = send_request(url, proxy)
    headers = {'User-Agent': random.choice(user_agents)}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    cms = None
    tech_stack = []

    # CMS detection
    if b'wp-content' in response.content:
        cms = 'WordPress'
    elif b'media/jui' in response.content:
        cms = 'Joomla'
    elif b'sites/all' in response.content:
        cms = 'Drupal'
    elif b'cdn.shopify.com' in response.content:
        cms = 'Spotify'
    elif b'js/mage' in response.content:
        cms = 'Magento'
    elif b'vbulletin' in response.content:
        cms = 'vBulletin'
    else:
        cms = 'Unknown'

    # Technology stack detection
    if b'PHP' in response.headers.get('content-type', '').encode():
        tech_stack.append('PHP')
    if b'python' in response.headers.get('content-type', '').encode():
        tech_stack.append('Python')
    if b'ASP.NET' in response.content:
        tech_stack.append('ASP.NET')
    if b'nginx' in response.headers.get('server', '').encode():
        tech_stack.append('nginx')
    if b'Apache' in response.headers.get('server', '').encode():
        tech_stack.append('Apache')
    if b'IIS' in response.headers.get('server', '').encode():
        tech_stack.append('IIS')
    if b'openresty' in response.headers.get('server', '').encode():
        tech_stack.append('Openresty')

    return cms, tech_stack

url = args.url
cms, tech_stack = detect_cms_and_tech_stack(url, proxy=None)
print("Content Management System:" + " " + cyan + "{}".format(cms) + RESET_ALL)
print("Technology Stack:" + " " + cyan + "{}".format(tech_stack) + RESET_ALL)


def is_valid_webpage(url):

    headers = {'User-Agent': random.choice(user_agents)}
    try:
       response = requests.get(url, headers=headers)
       #response = send_request(url, proxy=None)
       #response = requests.get(url, headers=headers)
       #response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        return False
    
    return response.status_code == 200



def is_valid_webpage_proxy(url):
    
    for proxy in proxy_list:
        headers = {'User-Agent': random.choice(user_agents)}
        try:
        # Send the request using the current proxy
            response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})

        except requests.exceptions.RequestException as e:
        # Print an error message if the request failed
            print(e)
            return False
            print("Request failed for proxy:", proxy)
    return response.status_code == 200



# Connect through Tor network
if args.tor:
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

# Read the website list from file
with open('ANTS/ants.txt', 'r') as f:
    website_list = f.read().splitlines()
 
    admin_count = 0
    total_count = len(website_list)
    pbar = tqdm(
            total=total_count,
            leave=False,
            bar_format=(

            ),
        )
# Iterate through each website in the list
for website in website_list:
    url = args.url + website
    pbar.update()
    if args.proxy: 
        if is_valid_webpage_proxy(url):
             tqdm.write(yellow + f"\n ҂ Found: {url}  " + RESET_ALL)

             admin_count += 1
    else:
        if is_valid_webpage(url):
             tqdm.write(yellow + f"\n ҂ Found: {url}  " + RESET_ALL)

             admin_count += 1
    if args.delay:
        time.sleep(args.delay * 60)

pbar.close()
print("\n\n\t╔═══[✔️]", green, BOLD, " Completed", RESET_ALL)
print("\t╟───╸📑️", str(admin_count), "Admin pages found")
print("\t╚═══[📚️]", str(total_count), "total pages scanned")
