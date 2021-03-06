﻿# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib2 import urlopen
from xml.etree import ElementTree

from botmily import irc

def stock(message_data, bot):
    result = urlopen('http://www.google.com/ig/api?stock=' + message_data["parsed"])
    root = ElementTree.fromstring(result.read())
    finance = root.find('finance')
    company = finance.find('company').get('data')
    currency = finance.find('currency').get('data')
    last = finance.find('last').get('data')
    change = finance.find('change').get('data')
    perc_change = finance.find('perc_change').get('data')
    trade_timestamp = finance.find('trade_timestamp').get('data')
    string = company + ' - '
    string += last + ' '
    string += currency + ' '
    change_string = change + ' (' + perc_change + ')'
    if change:
      if change[0] == '-':
          string += irc.color(change_string, 'brown')
      else:
          string += irc.color(change_string, 'green')
      string += ' as of '
      string += trade_timestamp
    return string

commands = {"stock": stock}
triggers = []

