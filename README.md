This is the FoCo nutrition app API. 

The FoCo nutrition app is the food diary I've always wanted: https://github.com/deloschang/foco-nutrition-scraper

The app makes requests to this API for daily menu items and associated
nutrition information for these items.

This app uses this information to create a 'food diary' where Dartmouth
students can track exactly how much macronutrients they are intaking
everyday.

====
Make a request like so:
http://localhost:8000/api/year/month/day/

So for example:
http://localhost:8000/api/2013/3/28/
