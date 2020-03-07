#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Colin Pollock"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Los_Angeles"
DEFAULT_LANG = "en"

THEME = "brutalist"
FIRST_NAME = "Colin"
GITHUB = "https://github.com/colinpollock"

MENUITEMS = [("tags", "/tags")]


# Using some URL scheme settings from https://github.com/j127/pelican_blog_project_template/blob/master/pelicanconf.py
PAGE_URL = "pages/{slug}"
ARTICLE_URL = "{slug}"
TAG_URL = "tag/{slug}"
CATEGORY_URL = "category/{slug}"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (
    ("github", "https://github.com/colinpollock"),
    ("linkedin", "https://www.linkedin.com/in/pollockcolin/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
