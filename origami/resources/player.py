"""Player resource."""

import json
import logging

import falcon

from ..db import PlayerDao

logger = logging.getLogger("main.player")
logger.setLevel(logging.DEBUG)


class Item(object):
    """Class representing an origami app player."""

    def on_get(self, req, resp, player_id):
        """Get a single player."""
        player_orm = PlayerDao.get_by_id(player_id, self.session)

        if player_orm:
            player = player_orm.as_dict

            resp.body = json.dumps(player, ensure_ascii=False)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404


class Collection(object):
    """Class to manage REST requests for the Player collection."""

    def on_get(self, req, resp):
        """Called on a GET for the collection."""
        players_orm = PlayerDao.get_list(self.session)
        players = [player.as_dict for player in players_orm]

        resp.body = json.dumps(players, ensure_ascii=False)
        resp.status = falcon.HTTP_200
