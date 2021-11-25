from server import loadClubs, loadCompetitions
from tests.test_unit.conf_test import client


class TestConnectLogout:
    def setup_method(self):
        """
        Allows to retrieve the real data of the application from the json files.
        We also generate bad information to simulate a wrong user input.
        :return:
        """
        self.clubs = loadClubs()
        self.competitions = loadCompetitions()

    def test_connect(self, client):
        """
        test if the user enters a good email address
        """
        response = client.post('/showSummary', data={'email': self.clubs[0]['email']})
        assert response.status_code == 200
        assert str.encode(self.clubs[0]['email']) in response.data
        response = client.get('/logout', follow_redirects=True)
        assert b'Welcome to the GUDLFT Registration Portal!' in response.data
