import os
import pygeoip

# Function to check if the GeoLiteCity database is available
def check_db():
    if not os.path.exists('GeoLiteCity.dat'):
        print("GeoLiteCity database not found.")
        print("Please download it from: https://dev.maxmind.com/geoip/geolite2-free-geolocation-data?lang=en")
        return False
    return True

# Check if database is available
if not check_db():
    exit()

# Initialize GeoIP object with the GeoLite database
gi = pygeoip.GeoIP('GeoLiteCity.dat')

# Ask user to input an IP address
ip = input('Please enter an IP address: ')

# Lookup record by IP address
record = gi.record_by_addr(ip)

if record:
    city = record.get('city', 'N/A')
    country = record.get('country_name', 'N/A')
    zipcode = record.get('postal_code', 'N/A')

    # Print the results
    print(f'IP Address: {ip}')
    print(f'City: {city}')
    print(f'Country: {country}')
    print(f'Zip Code: {zipcode}')
else:
    print(f'No information found for IP {ip}')