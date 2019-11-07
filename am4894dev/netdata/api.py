import requests


def get(endpoint='info', options='', ip='london.my-netdata.io', port='', api_version='v1/', return_json=True):
    """Make REST API request to a netdata.

    :param endpoint: Endpoint to call.
    :param options: Optional params for api.
    :param ip: What netdata to pull from.
    :param port: What port to pull from.
    :param api_version: Netdata API version to use
    :param return_json: If you want to get back json instead of a requests object.
    :return: Response which is either json or a requests response object.
    """

    # build request url
    base_url = f'https://{ip}:{port}/api/'
    request_url = f'{base_url}{api_version}{endpoint}{options}'

    # make request
    response = requests.get(request_url)

    # return response
    if return_json:
        return response.json()
    else:
        return response


def get_from_info(info, to_get='collectors'):
    """Take in an info response and pull back something interesting from it.

    :param info:
    :param to_get:
    :return:
    """

    if to_get == 'collectors':
        res = ['__'.join((p.get('plugin'), p.get('module'))) for p in info.get('collectors')]
    else:
        raise NotImplementedError(f"... to_get='{to_get}' not implemented ...")

    return res
