import requests

def get_unemployment_rate():
    """
    Returns the current US unemployment rate
    """
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/LNS14000000"
    headers = {
        "Content-type": "application/json"
    }
    data = """
    {
        "registrationkey": "YOUR_API_KEY",
        "startyear": "2022",
        "endyear": "2022"
    }
    """
    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    unemployment_rate = float(json_data["Results"]["series"][0]["data"][0]["value"])
    return unemployment_rate
