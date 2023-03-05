import requests

def get_labor_participation_rate():
    """
    Returns the current US labor force participation rate
    """
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/LNS11300000"
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
    labor_participation_rate = float(json_data["Results"]["series"][0]["data"][0]["value"])
    return labor_participation_rate
