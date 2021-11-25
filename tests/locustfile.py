from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def on_start(self):
        response = self.client.get("/")

    @task
    def showsummary(self):
        response = self.client.post('/showSummary', data={'email': 'john@simplylift.co'})

    @task
    def book(self):
        response = self.client.get('/book/Spring%20Festival/Simply%20Lift')

    @task
    def purchasePlaces(self):
        response = self.client.post('/purchasePlaces', data=dict(
            competition="Spring Festival",
            club="Simply Lift",
            places="3"
        ))

    @task
    def show_all_clubs_points(self):
        response = self.client.get('/clubs')

    @task
    def on_stop(self):
        response = self.client.get('/logout')
