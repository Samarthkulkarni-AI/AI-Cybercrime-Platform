import requests

def geocode_address(address, city, state, pincode):
    query = f"{address}, {city}, {state}, {pincode}"
    print(f"Querying: {query}")
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': query,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'CyberCrimeDashboard/1.0 (test script)'
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return float(data['lat']), float(data['lon'])
    except Exception as e:
        print(f"Geocoding error: {e}")
    return None, None

# Test with the user's address
lat, lon = geocode_address("Chintamani Nagar Phase 2", "Bibwewadi", "Maharashtra", "411037")
print(f"Result: {lat}, {lon}")

# Test with a simple address
print("\nTesting simple address:")
lat, lon = geocode_address("Pune", "Pune", "Maharashtra", "411001")
print(f"Result: {lat}, {lon}")
