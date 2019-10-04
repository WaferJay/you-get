#!/usr/bin/env python

import unittest

from you_get.extractors import (
    missevan
)


class YouGetTests(unittest.TestCase):

    def test_missevan(self):
        missevan.download('https://m.missevan.com/sound/1285995', info_only=True)
        missevan.download_playlist(
            'https://www.missevan.com/mdrama/drama/18129', info_only=True)

if __name__ == '__main__':
    unittest.main()
