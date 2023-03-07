import requests
from bs4 import BeautifulSoup


def search_products(query):
    """
    Searches for products on Google Shopping and returns a list of results
    """
    # Build the Google Shopping search URL
    url = f"https://www.google.com/shopping?q={query}&hl=en-US"

    # Send a request to the URL and get the response
    response = requests.get(url)

    # Use BeautifulSoup to parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all product results on the page
    product_results = soup.find_all('div', class_='pslires')

    # Create a list to store the product data
    products = []

    # Loop through each product result and extract the data
    for result in product_results:
        # Get the product title
        title = result.find('div', class_='psliresc').get_text(strip=True)

        # Get the product price
        price = result.find('span', class_='a8Pemb').get_text(strip=True)

        # Get the product image URL
        image_url = result.find('img')['src']

        # Get the product link URL
        link_url = result.find('a')['href']

        # Add the product data to the products list
        products.append({
            'title': title,
            'price': price,
            'image_url': image_url,
            'link_url': link_url
        })

    # Return the list of products
    return products


def search_stores(query):
    """
    Searches for stores on Google and returns a list of results
    """
    # Build the Google search URL
    url = f"https://www.google.com/search?q={query}+store&hl=en-US"

    # Send a request to the URL and get the response
    response = requests.get(url)

    # Use BeautifulSoup to parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all store results on the page
    store_results = soup.find_all('div', class_='g')

    # Create a list to store the store data
    stores = []

    # Loop through each store result and extract the data
    for result in store_results:
        # Get the store title
        title = result.find('h3').get_text(strip=True)

        # Get the store URL
        link_url = result.find('a')['href']

        # Add the store data to the stores list
        stores.append({
            'title': title,
            'link_url': link_url
        })

    # Return the list of stores
    return stores
