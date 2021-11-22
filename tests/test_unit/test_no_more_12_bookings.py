from server import loadClubs, loadCompetitions
from tests.test_unit.conf_test import client


class TestPurchaseMoreTwelve:
    def setup_method(self):
        """
        Allows to retrieve the real data of the application from the json files.
        We also generate bad information to simulate a wrong user input.
        :return:
        """
        self.clubs = loadClubs()
        self.competitions = loadCompetitions()

    def test_more_12_bookings(self, client):
        """
        test if the user enters more 12
        """
        club = self.clubs[0]
        response = client.post('/purchasePlaces', data=dict(
            competition=self.competitions[1]['name'],
            club=club['name'],
            places='13'
        ), follow_redirects=True)
        point_club = str.encode(f"Points available: {club['points']}")
        point_competition = str.encode(f"Number of Places: {self.competitions[1]['numberOfPlaces']}")
        assert point_club in response.data
        assert point_competition in response.data
        assert b'You cannot reserve more than 12 places!' in response.data
        assert response.status_code == 200
