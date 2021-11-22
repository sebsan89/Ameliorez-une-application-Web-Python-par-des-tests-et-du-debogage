from server import loadClubs, loadCompetitions
from tests.test_unit.conf_test import client


class TestViewAllClubs:
    def setup_method(self):
        """
        Allows to retrieve the real data of the application from the json files.
        We also generate bad information to simulate a wrong user input.
        :return:
        """
        self.clubs = loadClubs()
        self.competitions = loadCompetitions()

    def test_feature_for_view_all_clubs_and_point_in_table(self, client):
        response = client.get('/clubs')
        name_club_1 = str.encode(f"<td>{self.clubs[0]['name']}</td>")
        name_club_2 = str.encode(f"<td>{self.clubs[1]['name']}</td>")
        assert b'View Clubs' in response.data
        assert response.status_code == 200
        assert name_club_1 in response.data
        assert name_club_2 in response.data
