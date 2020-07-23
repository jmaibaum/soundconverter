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


class Task():
    """Abstract class of a single task."""
    def __init__(self):
        """Create a Task. Call this in your derived class."""
        # In order to keep __init__ args clean for use in derived classes
        # and whatever they need in their constructor, set attributes in
        # setters instead.
        self.callback = lambda: None

    def progress(self):
        """Fraction of how much of the task is completed."""
        raise NotImplementedError()

    def cancel(self):
        """Stop execution of the task."""
        raise NotImplementedError()

    def run(self, callback):
        """Run the task.
        
        Parameters
        ----------
            callback : function
                Call this when done
        """
        raise NotImplementedError()

    # private

    def set_callback(self, callback):
        """Callback to be used when the task finishes.

        Don't overwrite this function.

        Make sure to call self.callback() when done in your inheriting class.
        """
        def callback_wrapped():
            # automatically provide self as argument
            return callback(self)
        self.callback = callback_wrapped
