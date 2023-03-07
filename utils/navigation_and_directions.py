import requests

class NavigationAndDirections:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/directions/json"
        
    def get_directions(self, origin, destination, mode='driving', avoid=None, units='metric', departure_time=None, arrival_time=None):
        """
        Get directions from origin to destination
        :param origin: starting location
        :param destination: destination location
        :param mode: mode of transport (driving, walking, bicycling or transit)
        :param avoid: features to avoid on route (tolls, highways, ferries or indoor)
        :param units: units of measurement (metric or imperial)
        :param departure_time: departure time (optional)
        :param arrival_time: arrival time (optional)
        :return: dictionary containing the response
        """
        params = {
            'key': self.api_key,
            'origin': origin,
            'destination': destination,
            'mode': mode,
            'units': units
        }
        
        if avoid:
            params['avoid'] = avoid
        
        if departure_time:
            params['departure_time'] = departure_time
            
        if arrival_time:
            params['arrival_time'] = arrival_time
            
        response = requests.get(self.base_url, params=params)
        data = response.json()
        
        if data['status'] == 'OK':
            return data['routes'][0]
        else:
            return None
        
    def get_distance_and_duration(self, origin, destination, mode='driving', avoid=None, units='metric', departure_time=None, arrival_time=None):
        """
        Get distance and duration from origin to destination
        :param origin: starting location
        :param destination: destination location
        :param mode: mode of transport (driving, walking, bicycling or transit)
        :param avoid: features to avoid on route (tolls, highways, ferries or indoor)
        :param units: units of measurement (metric or imperial)
        :param departure_time: departure time (optional)
        :param arrival_time: arrival time (optional)
        :return: dictionary containing the distance and duration
        """
        directions = self.get_directions(origin, destination, mode=mode, avoid=avoid, units=units, departure_time=departure_time, arrival_time=arrival_time)
        
        if directions:
            legs = directions['legs'][0]
            distance = legs['distance']['text']
            duration = legs['duration']['text']
            return {'distance': distance, 'duration': duration}
        else:
            return None
