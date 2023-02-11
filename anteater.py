import argparse
import requests
import random
import time
import socks
import socket
from bs4 import BeautifulSoup
from colorama import Fore, Style
import signal

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
 
signal.signal(signal.SIGINT, handler)

blue = Fore.BLUE
red = Fore.RED
cyan = Fore.CYAN
green = Fore.GREEN
magenta = Fore.MAGENTA
RESET = Fore.RESET
DIM = Style.DIM
NORMAL = Style.NORMAL
BOLD = Style.BRIGHT
RESET_ALL = Style.RESET_ALL


#def print_colored_text(text, color):
#    if color == "red":
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
        proxy_list = f.read().splitlines()
else:
    proxy_list = []

# Read the user agent list from file
#with open('user_agents.txt', 'r') as f:
    #user_agents = f.read().splitlines()
user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    ]

# Function to send a request to the website using a random user agent and proxy






def send_request(url, proxy=None):
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        if proxy:
            response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy})
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
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return False
    
    return response.status_code == 200



# Connect through Tor network
if args.tor:
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

# Read the website list from file
with open('/ANTS/ants.txt', 'r') as f:
    website_list = f.read().splitlines()

# Iterate through each website in the list
for website in website_list:
    url = args.url + website
    #print(f'Checking: {url}')
    
    if args.proxy:
        proxy = random.choice(proxy_list)
        #result = detect_cms_and_tech_stack(url, proxy)
        if is_valid_webpage(url):
        #if result:
             print(blue + f"\n ҂ Found: {url}  " + RESET_ALL)
             
            #print(f'Result: Valid ({result[0]}, {result[1]})')
        #else:
            #print(' ')
    else:
        #result = detect_cms_and_tech_stack(url)
        if is_valid_webpage(url):
        #print(f"\n{page_url} exists.")
        #if result:
        #    print(f'Result: Valid ({result[0]}, {result[1]})')
             #print(f"\n{url} exists.")
             print(blue + f"\n ҂ Found: {url}  " + RESET_ALL)
             
        #else:
           # print(' ')
    if args.delay:
        time.sleep(args.delay * 60)
