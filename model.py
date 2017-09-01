# Copyright 2013 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.appengine.ext import ndb
import hnhh

class Song(ndb.model):
    title = ndb.StringProperty()
    artist = ndb.StringProperty()
    featured = ndb.StringProperty()
    soundcloud = ndb.StringProperty()


def updateLatest():
    songs = hnhh.get_songs()

    for song in songs:
        song = Song(title=song[1],artist=song[2],featured=song[3],soundcloud=song[0])
        song.put()

def allLatest():
    songs = Song.query()

    if not songs:
        updateLatest()
        return Song.query()
    else:
        return songs


class Guest(ndb.Model):
    first = ndb.StringProperty()
    last = ndb.StringProperty()


def AllGuests():
    return Guest.query()


def UpdateGuest(id, first, last):
    guest = Guest(id=id, first=first, last=last)
    guest.put()
    return guest


def InsertGuest(first, last):
    guest = Guest(first=first, last=last)
    guest.put()
    return guest


def DeleteGuest(id):
    key = ndb.Key(Guest, id)
    key.delete()
