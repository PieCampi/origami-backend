"""Unittest."""

import falcon

from .base_test_class import OrigamiTestCase


class EndingsTestCase(OrigamiTestCase):
    """Class for testing endings."""

    url = "/endings"

    def test_get_endings_list(self):
        """Test for the GET at /endings."""
        result = self.simulate_get(self.url,
                                   headers={"Authorization": "Bearer " + self.token}).json
        target = [
            {
                "id": 1,
                "played_story_id": 1,
                "text": "La storia finisce bene."
            },
            {
                "id": 2,
                "played_story_id": 2,
                "text": "La storia finisce male."
            },
            {
                "id": 3,
                "played_story_id": 3,
                "text": "La storia finisce malissimo."
            },
            {
                "id": 4,
                "played_story_id": 4,
                "text": "La storia finisce così così."
            }
        ]

        self.assertEqual(target, result)

    def test_get_ending(self):
        """Test for GET at /endings/1."""
        result = self.simulate_get(self.url + "/1",
                                   headers={"Authorization": "Bearer " + self.token}).json
        target = {
            "id": 1,
            "played_story_id": 1,
            "text": "La storia finisce bene."
        }

        self.assertEqual(target, result)

    def test_get_ending_nonexistent(self):
        """Try to GET a nonexistent ending."""
        result = self.simulate_get(self.url + "/5",
                                   headers={"Authorization": "Bearer " + self.token}).status
        target = falcon.HTTP_404

        self.assertEqual(result, target)
