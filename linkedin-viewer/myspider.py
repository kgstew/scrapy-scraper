from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

import time
import random

class LinkedPySpider(InitSpider):
    name = 'LinkedPy'
    allowed_domains = ['linkedin.com']
    login_page = 'https://www.linkedin.com/uas/login'
    start_urls = ['https://www.linkedin.com/in/brianharris', 'https://www.linkedin.com/pub/kyle-stewart/11/44a/746', 'https://www.linkedin.com/in/johnclarkemills']

    def login(self, response):
        #"""Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'session_key': 'buffreak13@gmail.com', 'session_password': 'starfireponyunicorn'},
                    callback=self.check_login_response)

    def init_request(self):
        #"""This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def check_login_response(self, response):
        #"""Check the response returned by a login request to see if we aresuccessfully logged in."""

        if "Sign Out" in response.body:
			self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
			# Now the crawling can begin..

			return self.initialized() 

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")
            # Something went wrong, we couldn't log in, so nothing happens.

    def parse(self, response):
        print response
        rand_sleep = random.randrange(62,246)
        print rand_sleep
        time.sleep(rand_sleep)
        return 




