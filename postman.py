"""
Quora-GitHub/postman.py
=======================

This module implements the interactions with the GitHub API.
It also works as the manager of incoming data.
"""

import os
import csv
import time
import logging
import requests
import ConfigParser

CONFIG_FILE_PATH = './config/config.ini'
CSV_FILE_PATH = './data/results.csv'
STATS_FILE_PATH = './data/stats.csv'
LOG_FILE = './log/postman.log'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)


class Postman:

    def __init__(self):
        self.base_url = 'https://api.github.com/repos/'
        self.token = None

        self.stats_file = os.path.join(os.path.dirname(__file__), STATS_FILE_PATH)

        self.load_config()
        self.log_stats()

        self.processed = 0

    def load_config(self):
        """ Load the config token provided for preventing the API rate-limiting.
        """

        config = ConfigParser.ConfigParser()
        config.read(CONFIG_FILE_PATH)

        self.token = config.get('authentication', 'token')

    def log_stats(self):
        """ Creates the header row for target csv data file.
        """

        with open(os.path.abspath(self.stats_file), 'w') as stats_file:
            stats_file.write("repository_url, stars, languages\n")

    def url_decode(self, url):
        """ Returns owner and repo name for a repository.
        """

        return url[19:].split('/')

    def url_encode(self, org, repo):
        """ Returns the repository url from organization and repo name.
        """

        return "https://github.com/{0}/{1}".format(org, repo)

    def process(self):
        """ Process the available repository url's and store the results.
        """

        with open(CSV_FILE_PATH) as csv_file:
            reader = csv.DictReader(csv_file)

            counter = 0

            # iterate over all the rows in .csv data file
            for row in reader:
                decoded_url = self.url_decode(row['repository_url'])
                org, repo = decoded_url[0], decoded_url[1]
                stars = row['stars']

                counter += 1
                self.processed += 1

                self.stats(org, repo, stars, self.processed)

                # one more hack to mitigate API-rate-limiting
                if (counter == 50):
                    time.sleep(10)
                    counter = 0

    def save_stats(self, org, repo, stars, languages):
        """ Store the final language statistics for a repository.
        """

        with open(os.path.abspath(self.stats_file), 'a') as stats_file:
            url = self.url_encode(org, repo)
            stats_file.write("{0}, {1}, {2}\n".format(url, stars, languages))

    def stats(self, org, repo, stars, processed):
        """ Interact with GitHub API for language statistics of a repository.
        """

        headers = {'Authorization': "token %s" % (self.token)}
        response = requests.get("%s%s/%s/languages" % (self.base_url, org, repo), headers=headers)

        if (response.status_code == requests.codes.ok):
            try:
                self.save_stats(org, repo, stars, len(response.json()))
            except:
                pass
        else:
            logging.error("{0} {1} {2}".format(org, repo, response.status_code))

        logging.info("row : {0}".format(processed))


if __name__ == '__main__':
    postman = Postman()
    postman.process()
