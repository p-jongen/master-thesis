import requests

def get_location(ip_address):
    API_KEY = "a5355d87ebbb32"
    url = f"https://ipinfo.io/{ip_address}/json?token={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["city"], data["region"], data["country"]
    else:
        return None, None, None

def get_ip_range(start, end):
    start_parts = start.split(".")
    end_parts = end.split(".")
    for i in range(int(start_parts[3]), int(end_parts[3]) + 1):
        yield f"{start_parts[0]}.{start_parts[1]}.{start_parts[2]}.{i}"

def search_ip_range(start, end):
    for ip in get_ip_range(start, end):
        city, region, country = get_location(ip)
        if city:
            print(f"{ip}: {city}, {region}, {country})
            
        else:
            print(f"{ip}: location not found")

start = "206.224.65.0"
end = "206.224.65.255"
search_ip_range(start, end)