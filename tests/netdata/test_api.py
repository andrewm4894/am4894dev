#!/usr/bin/env python
# -*- coding: utf-8 -*-

from am4894dev.netdata.api import get, get_from_info

# make request
TEST_INFO = get('info')
TEST_ALLMETRICS = get('allmetrics',return_type='text')


def test_api_get_info():
    """Default should return mirrored host as london3.my-netdata.io
    """
    assert TEST_INFO['mirrored_hosts'][0] == 'london3.my-netdata.io'


def test_api_get_allmetrics():
    """Ensure allmetrics response looks valid
    """
    assert "# chart:" in TEST_ALLMETRICS


def test_api_get_info_collectors():
    """Ensure length of collectors is positive
    """
    assert len(get_from_info(TEST_INFO,'collectors')) >= 1

