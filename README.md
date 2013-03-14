newrelic-python-kata
==================

Using New Relic and Heroku see how many things you can find and fix to make this app perform fast!

Step 1
-------
Get the code. The code is waiting to be forked on [github](https://github.com/newrelic/newrelic-python-kata)

Step 2
-------
Create a virtualenv and install the dependencies.

     cd newrelic-python-kata
     python virtualenv.py venv
     source venv/bin/activate
     pip install -r requirements.txt

Step 3
-------
Install Newrelic agent.

     pip install newrelic     
     newrelic-admin generate-config <license-key> newrelic.ini

Open the newrelic.ini file for editing.
Set the "transaction_tracer.transaction_threshold" to 0.2

Set the NEW_RELIC_CONFIG_FILE environment variable.

     export NEW_RELIC_CONFIG_FILE=newrelic.ini 
     
Step 4
------
Initialize the database.

     python initialize_db.py

Start the app.

     newrelic-admin run-python manage.py run_gunicorn

Step 5
-------
Fix the code / Solve as many of the Katas as you can. 

1. Access the application http://localhost:8000
2. Generate traffic a.k.a. click around.
3. Discover a slow page.
4. Investigate the problem.
5. Resolve with code changes.
6. Restart application.

     Repeat...

Step 6
-------
Let us know how you did, what you liked or disliked, what helped you find problems or what were the challenges, what you like about New Relic and what you don't - we just want to hear from you and see what we can do to get better. We'll even send you something for demonstrating your geek super powers when you complete the Kata - just provide us with your [thoughts and a link to your forked repo](https://support.newrelic.com/home).
