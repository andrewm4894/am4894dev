import pandas as pd
import requests


def get(endpoint='info', options='', ip='london.my-netdata.io', port='', api_version='v1/', return_type='json'):
    """Make REST API request to a netdata.

    :param endpoint: Endpoint to call.
    :param options: Optional params for api.
    :param ip: What netdata to pull from.
    :param port: What port to pull from.
    :param api_version: Netdata API version to use
    :param return_type: If you want to get back json instead of a requests object.
    :return: Response which is either json or a requests response object.
    """

    # build request url
    base_url = f'https://{ip}:{port}/api/'
    request_url = f'{base_url}{api_version}{endpoint}{options}'

    # make request
    response = requests.get(request_url)

    # return response
    if return_type == 'json':
        return response.json()
    elif return_type == 'text':
        return response.text
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


def get_chart_data(
    chart='system.cpu', after=-600, before=0, points=600, group='average', data_format='csv',
    endpoint='info', options='', ip='london.my-netdata.io', port='', api_version='v1/', return_type='json'
):
    """

    :param chart:
    :param after:
    :param before:
    :param points:
    :param group:
    :param data_format:
    :param endpoint:
    :param options:
    :param ip:
    :param port:
    :param api_version:
    :param return_type:
    :return:
    """

    # build options
    options = f'?chart={chart}&after={after}&before={before}&points={points}&group={group}&format={data_format}'
    # get data
    data_raw = get(
        'data', options=options, return_type='text', ip=ip, port=port, api_version=api_version
    )

    # wrangle data
    data_list = data_raw.split('\r\n')
    data_colnames = data_list[0].split(',')
    data_list = data_list[1:-1]
    data_list = [row.split(',') for row in data_list]

    # make df
    df = pd.DataFrame(data_list, columns=data_colnames)

    return df
