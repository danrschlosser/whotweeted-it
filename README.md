#Who Tweeted it?

Have you ever wanted to have fun but didn't know how?
Here is the solution:

Installation
--------------------

###1. Install MongoDB:

On mac, if you have [homebrew](http://brew.sh/) this can be done with:

````shell
   ~$ brew install mongodb
````

On other platforms, follow the instructions [here](http://docs.mongodb.org/manual/installation/)

To run a mongodb instance, in terminal, type:

````shell
      ~$ mongod
````
this will have to be running for the app to interact with the database


###2. Install Requirements

Navigate to the whotweeted-it directory and with [pip](http://pip.readthedocs.org/en/latest/installing.html):

````shell
      ~$ pip install -r requirements.txt
````

###3. Populate the database:
The app works by pulling tweets from the twitter API into a mongodb database. 
This database has to be populated for the app to work. In general, a server
deployment of the app would run a cron job that updates the tweet database
every so often. For the initial run, one must do this manually:

In the backend directory: 

````shell
      ~$ python cronJobs.py 
````

###4. Run the app!

Back in the whotweeted-it directory:

````shell
      ~$ python main.py
````
View the site on http://localhost:5000   !

