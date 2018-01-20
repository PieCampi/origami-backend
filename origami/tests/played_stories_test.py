"""Unittest."""

import logging

import falcon

from .base_test_class import OrigamiTestCase


logger = logging.getLogger("main.test_played_story")
logger.setLevel(logging.DEBUG)

class PlayedStoriesTestCase(OrigamiTestCase):
    """Class for testing played stories."""

    def test_get_playerd_stories_list(self):
        """Test for the GET at /played_stories."""
        result = self.simulate_get("/played_stories").json
        target = [
            {
                "played_story": 1,
                "player": [
                    {
                        "id": 1,
                        "name": "Gianni",
                        "age": 9,
                        "gender": "male"
                    }
                ],
                "choices": [2, 1],
                "ending": "La storia finisce bene."
            },
            {
                "played_story": 2,
                "player": [
                    {
                        "id": 2,
                        "name": "Federica",
                        "age": 8,
                        "gender": "female"
                    }
                ],
                "choices": [2, 3],
                "ending": "La storia finisce male."
            },
            {
                "played_story": 3,
                "player": [
                    {
                        "id": 1,
                        "name": "Gianni",
                        "age": 9,
                        "gender": "male"
                    }
                ],
                "choices": [3, 2],
                "ending": "La storia finisce malissimo."
            },
            {
                "played_story": 4,
                "player": [
                    {
                        "id": 3,
                        "name": "Josh",
                        "age": 6,
                        "gender": "male"
                    }
                ],
                "choices": [3, 1],
                "ending": "La storia finisce così così."
            }
        ]

        self.assertEqual(target, result)

    def test_get_played_story(self):
        """Test for GET at /played_stories/1."""
        result = self.simulate_get("/played_stories/1").json
        target = {
            "played_story": 1,
            "player": [
                {
                    "id": 1,
                    "name": "Gianni",
                    "age": 9,
                    "gender": "male"
                }
            ],
            "choices": [2, 1],
            "ending": "La storia finisce bene."
        }

        self.assertEqual(target, result)

    def test_get_played_story_nonexistent(self):
        """Try to GET a nonexistent played story."""
        result = self.simulate_get("/played_stories/5").status
        target = falcon.HTTP_404

        self.assertEqual(result, target)