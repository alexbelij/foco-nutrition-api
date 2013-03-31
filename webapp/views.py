# Create your views here.

from django.shortcuts import render_to_response

# algorithm imports
import urllib2, urllib2, json, httplib
import json

def api(request, month=None, day=None, year=None):

    # Dartmouth's nutrient aggregation to scrape


    # mm_id is available from the daily menu parse...
    # recipe_id is negative
    # mm_rank is provided too

    # able to change menu dates and access food listing for each date. 
    parameters = {"service":"","method":"get_recipes_for_menumealdate","id":11,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},
        "{\"menu_id\":\"27\",\"meal_id\":\"3\",\"remoteProcedure\":\"get_recipes_for_menumealdate\",\"day\":"+day+",\
                \"month\":"+month+", \"year\":"+year+",\"use_menu_query\":true,\"order_by\":\"pubgroup-alpha\",\"cache\":true}"]}

    # true parameters
    #parameters2 = {"service":"","method":"get_recipes_for_menumealdate","id":11,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},"{\"menu_id\":\"27\",\"meal_id\":\"3\",\"remoteProcedure\":\"get_recipes_for_menumealdate\",\"day\":27,\"month\":3,\"year\":2013,\"use_menu_query\":true,\"order_by\":\"pubgroup-alpha\",\"cache\":true}"]}
    

    # Beef Casserole code
    #parameters = {"service":"","method":"get_nutrient_label_items","id":17,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9786,\"recipe_id\":-473,\"mmr_rank\":165,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}

    # Constructed code for Chicken Tamale given the daily menu item -- successful
    #parameters = {"service":"","method":"get_nutrient_label_items","id":17,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9786,\"recipe_id\":-3755,\"mmr_rank\":737,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}


    #data = json.dumps(parameters)

    #headers = {"Content-Type": "application/json",
        #'Content-Length' : len(data),
        #"Referer":"http://nutrition.dartmouth.edu:8088/",
        ##"Cookie":'JSESSIONID=2C6BBA00328C1C2F67794E50337D6E3A.N1TS002',
        #"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
        #"method":"get_nutrient_label_items",
        #"params": "",
        #"id":25 # why static?
    #}

    #req = urllib2.Request(url, data, headers)
    #response = urllib2.urlopen(req)

    #daily_meal_menu = response.read()
    daily_meal_menu = make_request(parameters)

    daily_meal_menu = json.loads(daily_meal_menu)
    
    # copy the menu first
    menu_with_nutrients = daily_meal_menu
    read = daily_meal_menu

    recipes = daily_meal_menu['result']['recipeitems_list']

    for recipe in recipes: 
        print "Processing..." + recipe[0]

        # retrieve nutrient listing for each item
        recipe_id = recipe[1][3] * -1
        mmr_rank = recipe[1][4] 
        #print mmr_rank

        # 3/24
            # mm_id
                # lunch:  9772

        # 3/25
            # mm_id
                # lunch:  9750
        # 3/26 
            # mm_id
                # lunch:  9756

        # 3/27
            # mm_id
                # lunch:  9786
        # 3/28
            # mm_id
                # morning:9731
                # lunch:  9784
                # dinner: 9754
        # 3/29 
            # mm_id  
                # morning: 9769
                # lunch:   9745
                # dinner:  9770
            # mmr_rank   no change..

        # 3/30 
            # mm_id
                # morning: 9743
                # lunch:   9773 
                # dinner:  9729
        # 3/31
            # mm_id
                # lunch:   9764



            

        ## parameters for request


        ## mm_id changes everyday (with the menu) 
        # mm_id ==> 9786 to 9743 
        # mmr_rank ==> 146 from 271

        nutrient_parameters = {"service":"","method":"get_nutrient_label_items","id":17,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},
            "{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9773,\"recipe_id\":"+str(recipe_id)+",\"mmr_rank\":"+str(mmr_rank)+",\
                    \"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}

        recipe_nutrients = make_request(nutrient_parameters)

        read = recipe_nutrients
        

    return render_to_response('api.html', {'read':read,})

# make the request
def make_request(parameters):
    url = 'http://nutrition.dartmouth.edu:8088/cwp'

    data = json.dumps(parameters)

    headers = {"Content-Type": "application/json",
        'Content-Length' : len(data),
        "Referer":"http://nutrition.dartmouth.edu:8088/",
        #"Cookie":'JSESSIONID=2C6BBA00328C1C2F67794E50337D6E3A.N1TS002',
        "User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
        "method":"get_nutrient_label_items",
        "params": "",
        "id":25 # why static?
    }

    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    read = response.read()

    response.close()

    return read


# take in month, day, year and output JSON of each menu item's nutrition facts
def algorithm(month, day, year):
    pass

