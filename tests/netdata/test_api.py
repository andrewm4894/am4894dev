#!/usr/bin/env python
# -*- coding: utf-8 -*-

from am4894dev.netdata.api import get, get_from_info

# make request
TEST_INFO = get('info')


def test_api_get():
    """Default should return mirrored host as london3.my-netdata.io
    """
    res = TEST_INFO
    assert res['mirrored_hosts'][0] == 'london3.my-netdata.io'


def test_api_get_info():
    """Ensure length of collectors is positive
    """
    assert len(get_from_info(TEST_INFO,'collectors')) >= 1
