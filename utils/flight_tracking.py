import requests
import json

def track_flight(flight_number):
    """
    Track the flight information for a given flight number.
    
    Parameters:
        - flight_number (str): The flight number of the flight to track.
        
    Returns:
        - flight_data (dict): A dictionary containing the flight information.
    """
    
    # Request the flight data from the API
    url = f"https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{flight_number}"
    params = {
        "appId": "<YOUR_APP_ID>",
        "appKey": "<YOUR_APP_KEY>",
        "utc": "false"
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    
    # Extract the relevant flight information
    flight_status = data["flightStatuses"][0]["status"]
    departure_airport = data["flightStatuses"][0]["departureAirportFsCode"]
    departure_time = data["flightStatuses"][0]["departureDate"]["dateLocal"]
    arrival_airport = data["flightStatuses"][0]["arrivalAirportFsCode"]
    arrival_time = data["flightStatuses"][0]["arrivalDate"]["dateLocal"]
    
    # Create a dictionary containing the flight data
    flight_data = {
        "flight_status": flight_status,
        "departure_airport": departure_airport,
        "departure_time": departure_time,
        "arrival_airport": arrival_airport,
        "arrival_time": arrival_time
    }
    
    return flight_data
