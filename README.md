# language_data_collector
A website to collect sentence translations from the native speakers.

## To run
Setup and enter a python virtual enviroment.  
[Here is how to do it on ubuntu](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/)  
Now in the project folder (assuming python3 )
```
$ pip3 -r install requirements.txt
Followed by 
$ export FLASK_APP=web_app.py

You might wanna configure confiure.py as per your requirements
For the first time use, db migrations can be applied using
$ flask db upgrade

To run the app
$ flask run
```