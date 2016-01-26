#!/usr/bin/env python
# -*- conding: utf-8 -*-

from os import path
from IPython.display import HTML, display
from jinja2 import Environment, PackageLoader


class Sparkline(object):
    def __init__(self):
        self.env = Environment(loader=PackageLoader('ipython_sparkline', 'template', encoding='utf8'))

    def show(self, sparkline_data):
        template = self.env.get_template('sparkline.tpl.html')
        display(HTML(template.render({
            'data': sparkline_data
        })))
