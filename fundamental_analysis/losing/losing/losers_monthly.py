import requests
import datetime

API_URL = 'https://api.market.com/losers/monthly'

def get_top_losers(num):
    """
    Fetches the top N losers of the month from the market API.
    
    Args:
    num (int): The number of top losers to retrieve.
    
    Returns:
    A list of dictionaries, where each dictionary contains information about a company 
    that has experienced a loss in stock price over the month, sorted by the magnitude of the loss.
    """
    today = datetime.date.today()
    first_day_of_month = today.replace(day=1)
    response = requests.get(f'{API_URL}?num={num}&start_date={first_day_of_month}&end_date={today}')
    if response.ok:
        data = response.json()
        return sorted(data['losers'], key=lambda x: x['loss'], reverse=True)
    else:
        raise ValueError(f'Error fetching top {num} losers: {response.text}')

if __name__ == '__main__':
    num_top_losers = 10
    top_losers = get_top_losers(num_top_losers)
    print(f'Top {num_top_losers} losers of the month:')
    for i, company in enumerate(top_losers):
        print(f'{i+1}. {company["name"]}: {company["loss"]}%')
