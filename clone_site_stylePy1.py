import requests
from bs4 import BeautifulSoup

def clone_site_style(url):
    # Send a request to the website
    r = requests.get(url)

    # Parse the HTML of the website
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find all the CSS links on the website
    css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet')]

    # Download the CSS files
    css_data = ''
    for link in css_links:
        css_r = requests.get(link)
        css_data += css_r.text

    # Create the new HTML file
    html = '<html><head><style>' + css_data + '</style></head><body>' + soup.prettify() + '</body></html>'

    with open('cloned_site.html', 'w') as f:
        f.write(html)
        
#example usage
clone_site_style('https://example.com')
