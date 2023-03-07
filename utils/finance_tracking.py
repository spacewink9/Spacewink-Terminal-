import requests
from bs4 import BeautifulSoup
import datetime

class FinanceTracker:
    
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, stock):
        self.stocks[stock] = 0
        
    def remove_stock(self, stock):
        del self.stocks[stock]
        
    def update_stocks(self):
        for stock in self.stocks:
            # Use Yahoo Finance search for stock data
            url = f"https://finance.yahoo.com/quote/{stock}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract stock price
            price = soup.find_all("div", {"class": "D(ib) Mend(20px)"})[0].find_all("span")[0].text
            
            # Update stock price in the dictionary
            self.stocks[stock] = float(price.replace(",", ""))
        
    def get_portfolio_value(self):
        total_value = 0
        for stock, shares in self.stocks.items():
            total_value += self.stocks[stock] * shares
        return total_value
    
    def get_profit_loss(self, investment):
        current_value = self.get_portfolio_value()
        return (current_value - investment) / investment * 100
    
    def get_top_gainers(self, num=5):
        # Use Yahoo Finance search for top gainers data
        url = f"https://finance.yahoo.com/gainers"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract top gainers
        rows = soup.find_all("table")[0].find_all("tr")[1:]
        top_gainers = []
        for row in rows[:num]:
            name = row.find_all("td")[0].text.strip()
            change = row.find_all("td")[2].text.strip()
            top_gainers.append((name, change))
        return top_gainers
    
    def get_top_losers(self, num=5):
        # Use Yahoo Finance search for top losers data
        url = f"https://finance.yahoo.com/losers"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract top losers
        rows = soup.find_all("table")[0].find_all("tr")[1:]
        top_losers = []
        for row in rows[:num]:
            name = row.find_all("td")[0].text.strip()
            change = row.find_all("td")[2].text.strip()
            top_losers.append((name, change))
        return top_losers
    
    def get_news(self, stock):
        # Use Google search for stock news
        query = f"{stock} stock news"
        url = f"https://www.google.com/search?q={query}&tbm=nws"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract news articles
        articles = soup.find_all("div", {"class": "dbsr"})[:5]
        news = []
        for article in articles:
            title = article.find_all("div", {"class": "JheGif nDgy9d"})[0].text
            source = article.find_all("div", {"class": "XTjFC WF4CUc"})[0].text
            link = article.find_all("a")[0].get("href")
            date = article.find_all("div", {"class": "WW6dff uQIVzc Sksgp"})[0].text
"YMlKec fxKbKc"})[0].text
news.append({"title": title, "source": source, "link": link, "date": date})    # Return the news list
    return news
