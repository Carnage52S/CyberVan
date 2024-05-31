import pygeoip

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