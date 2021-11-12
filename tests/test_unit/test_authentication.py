from server import loadClubs, loadCompetitions


class TestAuthentication:
    def setup_method(self):
        """
        Allows to retrieve the real data of the application from the json files.
        We also generate bad information to simulate a wrong user input.
        :return:
        """
        self.clubs = loadClubs()
        self.competitions = loadCompetitions()
        self.bad_email_club = "test@error.com"  # bad email for testing with wrong input

    def test_if_bad_email_display_message_wrong_input(self, client):
        """
        test if the user enters a wrong email address
        """
        response = client.post('/showSummary', data={'email': self.bad_email_club})
        assert response.status_code == 200
        assert b'bad email' in response.data

    def test_if_good_email_for_authentication(self, client):
        """
        test if the user enters a good email address
        """
        response = client.post('/showSummary', data={'email': self.clubs[0]['email']})
        assert response.status_code == 200
        assert str.encode(self.clubs[0]['email']) in response.data
