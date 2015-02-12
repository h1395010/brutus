# -*- coding: utf-8 -*-

# Scrapy settings for brute_force project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'brute_force'

SPIDER_MODULES = ['brute_force.spiders']
NEWSPIDER_MODULE = 'brute_force.spiders'

ITEM_PIPELINES = {'brute_force.pipelines.BruteForcePipeline': 300 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'brute_force (+http://www.yourdomain.com)'
