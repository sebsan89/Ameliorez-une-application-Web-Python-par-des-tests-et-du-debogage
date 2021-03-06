import json
from datetime import datetime

from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        for competition in listOfCompetitions:
            if datetime.fromisoformat(competition['date']) < datetime.now():
                competition['completed'] = True
            else:
                competition['completed'] = False
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if club:
        return render_template('welcome.html', club=club[0], competitions=competitions)
    else:
        flash("You have entered a wrong email")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired < int(club['points']) \
            and placesRequired < int(competition['numberOfPlaces']) \
            and placesRequired <= 12:
        club['points'] = int(club['points']) - placesRequired
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        flash('Great-booking complete!')
    elif placesRequired > 12:
        flash("You cannot reserve more than 12 places!")
    else:
        flash("Reservation is impossible!")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/clubs')
def show_all_clubs_points():
    return render_template('clubs.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
