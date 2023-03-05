import requests

API_URL = 'https://api.market.com/insider-ownership'

def get_insider_ownership():
    """
    Fetches insider ownership information for all companies from the market API.
    
    Returns:
    A dictionary where the keys are the names of the companies and the values are dictionaries containing 
    information about insider ownership for the corresponding company, including the number of shares owned by insiders
    and the percentage of total shares outstanding owned by insiders.
    """
    response = requests.get(API_URL)
    if response.ok:
        data = response.json()
        ownership = {}
        for company_data in data:
            company_name = company_data['name']
            company_ownership = {
                'shares_owned': company_data['shares_owned'],
                'percent_outstanding': company_data['percent_outstanding']
            }
            ownership[company_name] = company_ownership
        return ownership
    else:
        raise ValueError(f'Error fetching insider ownership information: {response.text}')

if __name__ == '__main__':
    insider_ownership = get_insider_ownership()
    for company_name, ownership_info in insider_ownership.items():
        shares_owned = ownership_info['shares_owned']
        percent_outstanding = ownership_info['percent_outstanding']
        print(f'Insider ownership information for {company_name}: {shares_owned} shares owned ({percent_outstanding}% of outstanding shares)')
