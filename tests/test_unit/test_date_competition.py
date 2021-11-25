from server import loadClubs, loadCompetitions
from tests.test_unit.conf_test import client


class TestDate:
    def setup_method(self):
        """
        Allows to retrieve the real data of the application from the json files.
        We also generate bad information to simulate a wrong user input.
        :return:
        """
        self.clubs = loadClubs()
        self.competition = {
            "name": "Test Date",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }

    def test_not_purchase_competition_if_date_passed(self, client):
        response = client.post('/showSummary', data={'email': self.clubs[0]['email']})
        assert b'Spring Festival' in response.data
