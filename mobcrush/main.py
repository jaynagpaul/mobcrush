"""
mobcrush.main
~~~~~~~~~~~~~
Main file for the Mobcrush API
"""

import requests
from . import datatypes

BASE_URL = 'https://www.mobcrush.com/api/'


def _req(endpoint):
    """Sends a GET request to the API endpoint.
    :param endpoint: Endpoint to query.
    :type method: str
    :return: Parsed JSON object.
    :rtype: dict
    """
    data = requests.get(BASE_URL + endpoint)
    data.raise_for_status()
    return data.json()


def streamer(streamer):
    """Fetches streamer from api from username. Usernames must match the url of the streamer
    :param streamer: Streamer's username to query.
    :type method: str
    :return: mobcrush.Streamer.
    :rtype: class
    """
    data = _req('channel/web/{}/'.format(streamer))
    return datatypes.Streamer(data)


class User:
    """User class of the mobcrush api.
    :param username: Username of the user.
    :type username: str
    :param password: Password of the user. 
    :type password: str
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        """
        Fetches login info for the user
        """
        params = {'username': self.username, 'password': self.password}
        self.ses = requests.session()
        res = self.ses.post(BASE_URL + 'user/login', params=params)
        if res.text == '{"app_error":"AUTH_INVALID"}':
            raise ValueError('Incorrect Username or Password')
        else:
            self.cookies = res.cookies

    def say(chatroomid, msg):
        """
        Sends message to the specified chatroom id.
        :param: chatroomid: ID of the Mobcrush chatroom to send to
        :type chatroomid: str
        :param msg: Message to send
        :type msg: str
        :return: True if completed
        :rtype bool
        """
        params = {'message_text': str(msg)}
        res = self.ses.post(BASE_URL + 'chatroom/{}/chatmessage'.format(str(chatroomid)),
                            cookies=self.cookies, params=params)
        errors = res.json()['errors']
        if len(errors) == 0:
            return True
        else:
            raise ValueError(errors)


# TODO
# GET SEARCH https://www.mobcrush.com/api/search/global?limit=5&page=0&search=s
# GET BULK PRESENCE https://www.mobcrush.com/api/chatroom/1491700524639002000/bulkpresence?_c=1494129981094&uid=user%2F1491702904709003000&uid=user%2F1490531724235003000&uid=user%2F1491734890329000000&uid=user%2F1480647465816002000&uid=user%2F1464001356428000000&uid=user%2F1489936381238003000&uid=user%2F1464013039889000000&uid=user%2F1464007496846000000&uid=user%2F1471701813385002000&uid=user%2F1463995448977000000&uid=user%2F1464014643850000000
# GET PRESENCE https://www.mobcrush.com/api/chatroom/1491700524639002000/presence?_c=1494129982512&pageNum=2&pageSize=500
# DELETE SETTINGS https://www.mobcrush.com/api/auth/base/permission/chatroom/1478313289523001000/_/whisper_sender
# PUT NOIDEA https://www.mobcrush.com/api/pubsub/subscriber/1494130281102000000/topic/userMembershipChange/chatroom/1463972934909000000
# FOR WHISPERS IN PARAMS: parent_event_id: user/1476920128232010000
# FOR WHISPERS MULTI PART POST
# https://www.mobcrush.com/api/chatroom/1464005436201000000/chatmessage --
# POSSIBLY A USER ID OF SPIESBOT
# https://www.mobcrush.com/api/pubsub/subscriber/1494130691549001000/articles/head
# https://www.mobcrush.com/api/updateViewerCount - {broadcastId:
# "575869de73d71450aaa7d81a", incDec: "INC"}
# PUT - broadcastId: "575869de73d71450aaa7d81a"
# https://www.mobcrush.com/api/like
# GET VODS https://vodcdn.mobcrush.com/u/video/575869de73d71450aaa7d81a/recording.mp4Frag16Num16.
# VOD RECORDING https://cdn.mobcrush.com/u/video/575869de73d71450aaa7d81a/recording.mp4
# USER BY ID https://www.mobcrush.com/api/user/556d0e16eab733432e6d6721 = SpiesWithin ID
# Slow Mode - PUT to turn on - DELETE to turn off-  https://www.mobcrush.com/api/auth/base/permission/chatroom/1463972934909000000/add_msg/slow_mode
# PUT -
# DELETE MESSAGE
# https://www.mobcrush.com/api/chatroom/1463972934909000000/chatmessage/1486437940954003000
# message_text:
# parent_event_id: chatmessage / 1486437940954003000
# BAN - PUT -
# https://www.mobcrush.com/api/auth/membership/user/1476920128232010000/banned/chatroom/1463972934909000000
# CURRENT BROADCASTS https://api.mobcrush.com/broadcasts/0/30
# FOLLOWING https://api.mobcrush.com/followingBroadcasts/0/30
# POPULAR https://api.mobcrush.com/popularBroadcasts/0/30
# MENU GAMES https://api.mobcrush.com/menuGames
# SEARCH BY USER https://api.mobcrush.com/search/byUserList POST - FORMDATA regex: ^SpiesWithin
# SPOTLIGHT USERS https://api.mobcrush.com/featuredSpotlightUsers
# SEARCH BY USER https://api.mobcrush.com/search/byGameName POST - FORMDATA regex:
# CHANNEL BROADCASTS https://api.mobcrush.com/channelBroadcasts/556d0e16eab733432e6d6724/0/30
# IMAGE POST https://www.mobcrush.com/api/files/F7F9AFACBB4D7E95977F85FCD0E8400A Form data: F7F9AFACBB4D7E95977F85FCD0E8400A: ENCODEDIMAGE(PROBS GZIPPED)
# Stickers - ONLY NAME REALLY MATTERS - URL GETS IGNORED - requests.post('https://www.mobcrush.com/api/chatroom/1463972934909000000/chatmessage', cookies = m.cookies, params ={'message_text': '{"name":"ripley-rage","url":"https://cdn.mobcrush.com/static/com/mobcrush/images/mobcrush-icon.png","version":"20170110"}', 'content_type': 'application/x-mobcrush/sticker'})
# END LIST ===========
