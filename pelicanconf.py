#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Kenneth Kinyanjui'
SITENAME = u'iamkenju254.com'
SITEURL = ''

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'
#Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
            ('Archive', 'archives.html'),
            ('Tags', 'tags.html'),
            ('Projects', 'pages/projects.html'),
            ('Just Saying', 'pages/justsaying.html'),
            ('About', 'pages/about-me.html')]

DEFAULT_CATEGORY = 'Uncategorized'


DATE_FORMAT = {
    'en': '%d %m %Y'
}
DEFAULT_DATE_FORMAT = '%d %m %Y'

THEME = 'flasky'

DISQUS_SITENAME = 'iamkenju254com'
TWITTER_USERNAME = 'kenju254'
LINKEDIN_URL = 'http://ke.linkedin.com/pub/kenneth-mbugua-kinyanjui/30/8b7/975/'
GITHUB_URL = 'http://github.com/kenju254'
FACEBOOK_URL = 'http://www.facebook.com/kenmbugua'
GOOGLEPLUS_URL = 'https://plus.google.com/107572086363730112974/posts'
PINTEREST_URL = 'http://pinterest.com/kenju254'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = '/output'

GOOGLE_ANALYTICS_ACCOUNT = 'UA-00000000-1'

PIWIK_URL = 'myurl.com/piwik'
PIWIK_SSL_URL = 'myurl.com/piwik'
PIWIK_SITE_ID = '1'

MAIL_USERNAME = 'kenmbugua'
MAIL_HOST = 'gmail.com'

# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)