from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Email
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'poiuytrewq'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name')  # add validators
    location = StringField('Cafe Location (Google map link)')
    open_time = StringField('Opening Time eg. 8AM')
    closing_time = StringField('Closing Time eg. 8PM')
    coffee_rating = SelectField('Coffee Ratings', choices=[(1, '☕'), (2, '☕☕'), (3, '☕☕☕'), (4, '☕☕☕☕')])
    wifi = SelectField('Wifi Strength', choices=[(1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '✘')])
    power = SelectField('Power Socket Availability', choices=[(1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌')])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("form In side", form.cafe)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
