# -*- coding: utf-8 -*-
"""
mobcrush.datatypes
~~~~~~~~~~~~~~~~~~

Datatypes for the Mobcrush API.
"""


class Game:
    """Class for mobcrush games

    :param data: Data of the game
    :type data: dict
    """

    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.data.get('_id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def icon(self):
        return self.data.get('icon')

    @property
    def urls(self):
        return self.data.get('urls')


class Broadcast:
    """Class for mobcrush broadcasts

    :param data: Data of the broadcast
    :type data: dict
    """

    def __init__(self, data):
        self.b = data  # broadcast

    @property
    def region(self):
        return self.b.get('regionName')

    @property
    def id(self):
        return self.b.get('_id')

    @property
    def game(self):
        return Game(self.b.get('game', {}))

    @property
    def startdate(self):
        return self.b['startDate']

    @property
    def enddate(self):
        return self.b['startDate']

    @property
    def user(self):
        return self.b['user']['username']

    @property
    def url(self):
        return self.b['user']['url']

    @property
    def mature(self):
        return self.b.get('mature', False)

    @property
    def formats(self):  # Video formats. I think
        return self.b.get('storageFormats')

    @property
    def views(self):
        return self.b.get('totalViews')

    @property
    def likes(self):
        return self.b.get('likes')

    @property
    def title(self):
        return self.b.get('title')

    @property
    def live(self):
        return self.b.get('isLive', False)

    @property
    def viewers(self):  # Current viewers
        return self.b.get('currentViewers')

    @property
    def hasCustomThumbnail(self):
        return self.b.get('hasCustomThumbnail', False)

    @property
    def height(self):
        return self.b.get('height')

    @property
    def width(self):
        return self.b.get('width')

    @property
    def snapshot(self):
        return 'http://cdn.mobcrush.com/u/video/{}/snapshot.jpg'.format(self.id)


class Streamer:
    """Class for streamers

    :param data: Data of the streamer
    :type data: dict
    """

    def __init__(self, data):
        # Left as standard dict notation purposely
        self.user = data['users'][0]
        self.data = data
        self.userobj = self.user['user']
        self.lb = self.user.get('lastBroadcast', {})  # Last broadcast
        self.lbuser = self.lb.get('user', {})

    @property
    def name(self):
        return self.userobj.get('username')

    @property
    def followercount(self):
        return self.userobj.get('followerCount')

    @property
    def followingcount(self):
        return self.userobj.get('followingCount')

    @property
    def broadcastcount(self):
        return self.userobj.get('broadcastCount')

    @property
    def profilepic_s(self):  # Small profile picture
        return self.userobj.get('http://cdn.mobcrush.com/u/profile/57096903684f71a8327e9f01/54454c6834_s.jpg')

    @property
    def id(self):
        return self.userobj.get('_id')

    @property
    def chatroomid(self):  # Extracts num from chatroom/{{id}}
        return filter(str.isdigit, self.user.get('chatroomObjectId'))

    @property
    def islive(self):
        return self.user.get('isLive', False)

    @property
    def donations(self):
        return self.userobj.get('enableDonations', False)

    @property
    def subtitle(self):
        return self.userobj.get('subtitle')

    @property
    def featured(self):
        return self.userobj.get('influencerAttributes').get('spotlight')

    @property
    def description(self):
        return self.data['channel'].get('description')

    @property
    def poster(self):  # Poster image displayed when channel is offline
        return self.data['channel'].get('offlinePosterImage')

    @property
    def partner(self):
        return self.lbuser.get('isPartner')

    @property
    def profilepic(self):
        return self.lbuser.get('profileLogo')

    @property
    def lastbroadcast(self):
        return Broadcast(self.lb)

    @property
    def raw(self):
        return self.data

    @property
    def url(self):  # Url of the channel
        return self.data['channel'].get('url')
