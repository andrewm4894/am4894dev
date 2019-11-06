#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest 

from am4894dev.netdata.api import get

def test_api_get():
    res = get()
    assert res['mirrored_hosts'][0] == 'london3.my-netdata.io'