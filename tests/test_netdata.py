#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest 

import am4894dev.netdata as nd

def test_api_get():
    res = nd.api.get()
    assert res['mirrored_hosts'][0] == 'london3.my-netdata.io'