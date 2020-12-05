#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'evg-dev'
SITENAME = 'Developer HandBook'
SITEURL = '/'

PATH = 'content'
THEME = 'theme/simple-bootstrap-custom'
TIMEZONE = 'Asia/Yekaterinburg'


RELATIVE_URLS = False

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}.html'

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

# PAGE_URL = CATEGORY_URL + '/{slug}/'
# PAGE_SAVE_AS = CATEGORY_URL + '/{slug}/index.html'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
