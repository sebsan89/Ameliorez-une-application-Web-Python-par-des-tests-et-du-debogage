from server import loadClubs, loadCompetitions
from tests.test_unit.conf_test import client


class TestPurchase:
    def setup_method(self):
        """
        Allows to retrieve the real data of the application from the json files.
        We also generate bad information to simulate a wrong user input.
        :return:
        """
        self.clubs = loadClubs()
        self.competitions = loadCompetitions()

    def test_more_purchase_than_point(self, client):
        """
        test if the user enters more than point available
        """
        club = self.clubs[1]
        points = int(club['points']) + 2
        response = client.post('/purchasePlaces', data=dict(
            competition=self.competitions[0]['name'],
            club=club['name'],
            places=str(points)
        ), follow_redirects=True)
        point_club = str.encode(f"Points available: {club['points']}")
        point_competition = str.encode(f"Number of Places: {self.competitions[0]['numberOfPlaces']}")
        assert point_club in response.data
        assert point_competition in response.data
        assert b'Reservation is impossible!' in response.data
        assert response.status_code == 200

    def test_purchase_ok_if_number_point_ok(self, client):
        """
        test if the user enters a good number
        """
        club = self.clubs[1]
        points = int(club['points']) - 2
        response = client.post('/purchasePlaces', data=dict(
            competition=self.competitions[0]['name'],
            club=club['name'],
            places=str(points)
        ), follow_redirects=True)
        search = str.encode(f"Points available: 2")
        assert search in response.data
        assert b'Great-booking complete!' in response.data
        assert response.status_code == 200
