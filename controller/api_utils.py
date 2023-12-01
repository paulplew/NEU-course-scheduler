import requests

class RequestFailedException(Exception):
    pass

def get(url, debug=False, **kwargs):
    if debug:
        print(f"fetching: {url}")
    response = requests.get(url, **kwargs)
    
    # 200 means good 
    if response.status_code == 200:
        return response
    else:
        raise RequestFailedException(f"Request failed with unknown status code: {response.status_code}")

def post(url, debug=False, **kwargs):
    if debug:
        print(f"POST: {url}")
        
    response = requests.post(url, **kwargs)

    if response.status_code == 200:
        return response
    else:
        raise RequestFailedException(f"Request failed with unknown status code: {response.status_code}")