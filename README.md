# UWaterloo-Nutritional-Meal-Finder
<h2>Synopsis</h2>
A meal finding script which can be used to find meals available on the University of Waterloo Campus that meet specific dietary specifications using the University of Waterloo Food Serices API. Users can specify whether they are interested in lunch or dinner options, if they have a specific diet type such as vegetarian, vegan, or halal, and set upper and lower limits for desired nutritional values including calories, fat, protein, carbohydrates, and sodium. After entering your search the meal names that meet your specifications as well as the food outlet location will be printed out. The exact amounts of each nutrient you created a limit for will also be interested in case you wish to compare options.  
<h2>Running the script</h2>
This script was written using Python 2.7 and is ran on the command line terminal. To be able to run this script you must have Python version 2 installed on your machine. To run the script you must first save the file mealfinder.py to a file on your machine. To run the script you must navigate to the file the script in located in using the command line terminal (BASH or Powershell). To execute the script   in the command line type:
<br>
<br>
Python mealfinder.py (your meal specifications go here – see below)
<br>
<h2>Meal specifications</h2>
When wishing to filter out meals there are 4 main search create that can be entered into the terminal. They are as follows:
<h4>Meal Type</h4>
You can choose to filter meals by <b>lunch</b> or <b>dinne</b>r type. To do this all you have to type is either lunch or dinner in the terminal. If you do not care about specifying meal type then you do not need to enter anything for meal type. 
<h4>Diet Type</h4>
There are 3 special diet types offered on campus: <b>vegetarian</b>, <b>vegan</b>, and <b>halal</b>. If you wish to find meals that are a specific meal type then you just need to type either vegetarian, vegan, or halal into the terminal. If you do not wish to specify a diet type than you do not need to enter anything. You can however not search for two diet types in a single script execution. 
<h4>Nutrient Values</h4> 
When searching for meals you can also set upper and lower limits on certain nutritional values. These include <b>calories</b>, <b>fat</b>, <b>protein</b>, <b>carbohydrates</b>, and <b>sodium</b>. This is written in the following format “Nutrient[lower,upper]". For example let say you want to find a meal that is between 300 and 600 calories and is over 20g of protein. In the terminal you would type:
<br>
<br>
calories[300,600] protein[20,]
<br>
<br>
Notice how the upper limit for protein is empty. Similarly the lower limit for a nutrient can also be empty if you do not wish to set one. All values you enter should be an integer (if not left empty). Be sure to also pay attention to the correct formatting and not add spaces. Protein, fat, and carbohydrates are entered in grams while sodium is measured in milligrams.
<h4>Date</h4>
This script will automatically look for foods available today, however if you wish to search for a different day to plan ahead you can enter a <b>date</b> into the terminal as well. A date must be written in the format YYYY-MM-DD. Keep in mind that campus food outlets are not open on weekends and that you cannot look too far ahead in the future as meal information is only provided for a certain amount of time in advance.
<h4>In review you have to option of entering the following specifications:</h4>

dinner or lunch
<br>
vegetarian, vegan, or halal
<br>
calories[lower,upper]
<br>
fat[lower,upper]
<br>
protein[lower,upper]
<br>
carbo[lower,upper]
<br>
sodium[lower,upper]
<br>
YYYY-MM-DD
<h2>Examples</h2>
Let’s say you are interested in looking for vegetarian options for dinner on September 27, 2015, that are above 15g of protein. What you would type into the command line terminal after navigating into the correct folder is:
<br>
<br>
Python mealfinder.py vegetarian dinner 2015-09-27 protein[15,]   
<br>
After hitting enter your results will be printed to the terminal.
