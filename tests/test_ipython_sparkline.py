#!/usr/bin/env python
# -*- conding: utf-8 -*-

from ipython_sparkline import Sparkline

def test_constructor():
    sl = Sparkline()
    assert hasattr(sl.show, '__call__')
