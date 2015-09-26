import sys
import requests
import json
import datetime

sysargv = sys.argv[1:]

param_dict = {}

date = datetime.date.today().strftime("%Y-%m-%d")

## Checks if input is in date form
def if_date(d):
	try:
		datetime.datetime.strptime(d, '%Y-%m-%d')
		return True
	except: 
		return False

## Organizes variables in sysargv into param_dict based on type
try:
	for x in sysargv:
		if x.lower() == 'lunch' or x == 'dinner':
			param_dict['meal_type'] = x
		elif x.lower() =='vegan' or x == 'vegetarian' or x == 'halal':
			param_dict['diet_type'] = x
		elif if_date(x) == True:
			date = x
		else:
			x = x.split("[")
			v = x[1].split(",")
			v[1] = v[1].replace("]","")
			param_dict[x[0]] = v
except:
	sys.exit("Check that your search criteria is entered correctly")
				

week = datetime.date(int(date.split("-")[0]),int(date.split("-")[1]),int(date.split("-")[2])).isocalendar()[1]
year = datetime.date(int(date.split("-")[0]),int(date.split("-")[1]),int(date.split("-")[2])).isocalendar()[0]
day = datetime.date(int(date.split("-")[0]),int(date.split("-")[1]),int(date.split("-")[2])).strftime('%A')

param_dict['day'] = day

menu = requests.get('https://api.uwaterloo.ca/v2/foodservices/' + str(year) + '/' + str(week) + '/menu.json?key=2385ec35f07bee1e3b7486cfadbefb37')

menu_dict = menu.json()

## Returns true if the value for each key in param_dict equals the corresponding meal value and/or all nutrient values in a meal 
## are within the limits for that nutrient defined in param_dict 
def meal_filter(meal):
	for k,v in param_dict.iteritems():
		if k == 'meal_type' or k == 'diet_type' or k == 'day':
			if getattr(meal,k)!=v:
				return False 
 		else:
			if v[0] != "" and getattr(meal,k) <= int(v[0]): 
				return False
			if v[1] != "" and getattr(meal,k) >= int(v[1]):
				return False
	return True

class Meal:
	'Fields: day, meal_type, diet_type, calories, fat, carbo, protein, sodium, location, name'
	def __init__(self, day, meal_type, diet_type, calories, fat, carbo, protein, sodium,location,name):
		self.day = day
		self.meal_type = meal_type
		self.diet_type = diet_type
		self.calories = calories
		self.fat = fat
		self.carbo = carbo
		self.protein = protein
		self.sodium = sodium 
		self.location = location
		self.name = name
	def __repr__(self): 
		return "day: {0.day}; meal_type: {0.meal_type}; diet type: {0.diet_type}; calories: {0.calories}; fat: {0.fat}; carbs: {0.carbo};\
		 protein: {0.protein}; sodium: {0.sodium}; location: {0.location}".format(self)

# Creates a list of Meal objects for meals available that day using weekly nutritional information
meal_list = []
for outlet in menu_dict['data']['outlets']:
	location = outlet['outlet_name']
	for item in outlet['menu']:
		week_day = item['day']
		if week_day == day:
			for meal in ['lunch','dinner']:
				for i in item['meals'][meal]:
					product_id = i['product_id']
					product_url = 'https://api.uwaterloo.ca/v2/foodservices/products/' + str(product_id) + '.json?key=2385ec35f07bee1e3b7486cfadbefb37'
					product_menu = requests.get(product_url)
					product_dict = product_menu.json()
					if product_id == None:
						i['product_name'] = Meal(week_day,meal,i['diet_type'], None, None, None, None, None,location,i['product_name'])
					else:
						i['product_name'] = Meal(week_day,meal,i['diet_type'], product_dict['data']['calories'], product_dict['data']['total_fat_g'], \
							product_dict['data']['carbo_g'], product_dict['data']['protein_g'], product_dict['data']['sodium_mg'],location,i['product_name'])
					meal_list.append(i['product_name'])

# Removes Meal objects that rertun False when passed through meal_filter 
try:
	result_list = (list(filter(meal_filter, meal_list)))
except:
	sys.exit("Check that your search entry is valid")

# Prints the Meal name and location as well as prints out the Meal values for variables the user specified 
for m in result_list:
	print m.name + " at " + m.location
	for k in param_dict:
		print k + ": " + str(getattr(m,k))


 