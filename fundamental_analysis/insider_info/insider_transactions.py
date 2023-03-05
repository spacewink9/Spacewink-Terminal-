import requests

API_URL = 'https://api.market.com/insider-info'

import requests

API_URL = 'https://api.market.com/insider-transactions'

def get_insider_transactions():
    """
    Fetches insider trading information for all companies from the market API.
    
    Returns:
    A dictionary where the keys are the names of the companies and the values are lists of dictionaries, 
    where each dictionary contains information about an insider trading activity for the corresponding company,
    sorted by the transaction date.
    """
    response = requests.get(API_URL)
    if response.ok:
        data = response.json()
        transactions = {}
        for company_data in data:
            company_name = company_data['name']
            company_transactions = sorted(company_data['transactions'], key=lambda x: x['transaction_date'])
            transactions[company_name] = company_transactions
        return transactions
    else:
        raise ValueError(f'Error fetching insider transactions: {response.text}')

if __name__ == '__main__':
    insider_transactions = get_insider_transactions()
    for company_name, transactions in insider_transactions.items():
        print(f'Insider trading information for {company_name}:')
        for transaction in transactions:
            print(f'{transaction["transaction_date"]}: {transaction["insider_name"]} {transaction["transaction_type"]} {transaction["shares"]} shares at {transaction["price_per_share"]}$')
    """
    Fetches insider trading information for a specific company from the market API.
    
    Args:
    company_name (str): The name of the company for which to retrieve insider trading information.
    
    Returns:
    A list of dictionaries, where each dictionary contains information about an insider trading activity 
    for the given company, sorted by the transaction date.
    """
    response = requests.get(f'{API_URL}?company={company_name}')
    if response.ok:
        data = response.json()
        return sorted(data['trades'], key=lambda x: x['transaction_date'])
    else:
        raise ValueError(f'Error fetching insider trades for {company_name}: {response.text}')

if __name__ == '__main__':
    company_name = 'ABC Corporation'
    insider_trades = get_insider_trades(company_name)
    print(f'Insider trading information for {company_name}:')
    for trade in insider_trades:
        print(f'{trade["transaction_date"]}: {trade["insider_name"]} {trade["transaction_type"]} {trade["shares"]} shares at {trade["price_per_share"]}$')
