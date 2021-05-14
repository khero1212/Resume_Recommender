# Resume_Recommender

A multi-class classifier from scratch that caters curated resumes using the Multinomial Naïve Bayes algorithm and deployed on heroku.

The app can be found at https://resume-classifier-1212.herokuapp.com/

# Working with the recommender

Make sure that you have python installed on your device. You can download python from:

https://www.python.org/downloads/ .

Then get “pip”, a package manager for python. You can find the documentation for installation here:

https://pip.pypa.io/en/stable/installing/

Now change your directory to the textClassifier directory using the command

`$ cd textClassifier`

Install all the dependencies to run the program using the command

`$ pip3 install -r requirements.txt`

To run and test the flask web app on your local host, run the command

`$ python3 api.py`

To verify this open a browser and go to http://localhost:5000/

Currently, I implemented integration tests to evaluate the api endpoint. I used the Pytest library to create these tests.

To run the tests, run the command

`$ pytest integration_tests.py`

You can also find this web app deployed on Heroku using the link: https://resume-classifier-1212.herokuapp.com/

#Note

Now, sometimes the deployed app might not run because I am using a free tier dyno version, so if you run into application error while accessing the app via Heroku then I suggest you to come back a few hours later to check out the app.

Currently the server side code is built using Flask, but some in the future I intend to replace the server infrastructe with Django.

