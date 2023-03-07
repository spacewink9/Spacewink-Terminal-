import requests
from bs4 import BeautifulSoup

def get_restaurant_data(city, cuisine):
    """
    Scrape data from Yelp to obtain restaurant data for a specific city and cuisine.
    """
    url = f"https://www.yelp.com/search?find_desc={cuisine}&find_loc={city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    restaurants = []
    for restaurant in soup.find_all("div", {"class": "lemon--div__373c0__1mboc searchResult__373c0__1yggB border-color--default__373c0__2oFDT"}):
        name = restaurant.find("h4", {"class": "lemon--h4__373c0__1yd__ heading--h4__373c0__2-XIO"}).get_text().strip()
        rating = float(restaurant.find("div", {"class": "lemon--div__373c0__1mboc i-stars__373c0__1T6rz rating__373c0__2LVZK"}).get("aria-label").split()[0])
        reviews = int(restaurant.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"}).get_text().split()[0])
        price = restaurant.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"}).get_text().strip()

        restaurants.append({"name": name, "rating": rating, "reviews": reviews, "price": price})

    return restaurants

def recommend_restaurants(city, cuisine, budget, rating_threshold):
    """
    Analyze restaurant data and recommend restaurants based on budget and rating threshold.
    """
    restaurants = get_restaurant_data(city, cuisine)
    recommended_restaurants = []

    for restaurant in restaurants:
        price = restaurant["price"].count("$")
        if price <= budget and restaurant["rating"] >= rating_threshold:
            recommended_restaurants.append(restaurant)

    return recommended_restaurants
