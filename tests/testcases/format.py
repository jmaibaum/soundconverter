#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# SoundConverter - GNOME application for converting between audio formats.
# Copyright 2004 Lars Wirzenius
# Copyright 2005-2020 Gautier Portet
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

import unittest
from soundconverter.util.formats import get_mime_type, get_quality


class Format(unittest.TestCase):
    def test_get_mime_type(self):
        self.assertEqual(get_mime_type('mp3'), 'audio/mpeg')
        self.assertEqual(get_mime_type('audio/x-m4a'), 'audio/x-m4a')

    def test_get_quality(self):
        self.assertEqual(get_quality('mp3', 0, 'cbr'), 64)
        self.assertEqual(get_quality('aac', 1, 'thetgdfgsfd'), 96)
        self.assertEqual(get_quality('aac', 256, reverse=True), 4)
        self.assertEqual(get_quality('mp3', 320, mode='abr', reverse=True), 5)


if __name__ == "__main__":
    unittest.main()
