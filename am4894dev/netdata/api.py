import requests

def get(endpoint='info',options='',ip='london.my-netdata.io',port='',api_version='v1/',return_json=True):
    # build request url
    base_url=f'https://{ip}:{port}/api/'
    request_url = f'{base_url}{api_version}{endpoint}{options}'
    # make request
    response = requests.get(request_url)
    # return response
    if return_json:
        return response.json()
    else:
        return response
