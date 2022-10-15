# Recipe Finder Application

#### Video Demo:  <TODO>

## Description:
This is my Recipe Finder App created using the Django Framework.
To run this application, python must be installed on your computer, along with these files in GitHub.

To start, run `python -m pip install Django` if django is not installed.

To open the website after Django is successfully installed on your computer,
run `python manage.py runserver` to start the application.

Look below for further details using Django if the commands fail.

#### Recipe Finder Application Features
For the project, the Recipe Finder Application allows a user to search for cooking recipes with parameters from user input using
the Spoonacular Recipe API. The user has many parameters to select from, including dietary restrictions, name of the recipe, and the
list of ingredients to consider. Once the search query has been initialized by the user, they will receive a feedback of the list of 
ingredients that the user has requested. Choosing a recipe from the search query will take the user to that specific requested recipe,
where further recipe details are explained - this includes cooking instructions, used ingredients, and comments left by other users of
the website.

Although the main purpose of the Recipe Finder Application is to query for cooking recipes, users can also dynamically interact with
the website, by favoriting recipes that they want to view for later, and leaving specific comments on certain recipes that they feel
strongly about that others can see. In addition, they can also subscribe to the website's newsletter, and also contact the creator
of the website (me) through a contact form on the webpage if they wish to do so.

#### Design Choices
I wanted to make a Recipe Finder because I wanted to create an application that featured the ability to query for recipes while it being
intuitive for other people to utilize. I believe this application gives users the flexibility to search for the recipes that they desire
with many query options.

Along with the design choices above, I also wanted the application to be more interactive between potential users, being able to communicate
with each other via comments on recipes (and possibily in the future, through their blog posts).

#### Navigating the Application
Starting the application, the user is first greeted by the login page - which they must register and log in to have access to the rest of the 
application. Once in the main page of the application, therer are many suggested recipes that the user can interact with, as well as a navigation 
bar to browse the different features and information regarding the website.

#### Possible Feature Creep in the Future
One major feature if there would be enough users is to add the ability for all the users to post their blogs or status updates to further 
increase the interactivity between different users. Right now the features regarding user interaction is limited - being able to comment 
on recipes and read what others have said as well. This may be done by refactoring the index to show a live feed for other users to see - 
almost like a social media website. Since the purpose of this application is to query for recipes, the feature has not been implemented 
as of yet.

#### Credits
This application contains static files and template files from these following websites: 
https://appseed.us
https://colorlib.com/ 

## Django CLI Commands

#### Verify Version
You can verify your Django installation by executing `django-admin --version` to check if you have the correct version.

#### Proxy
If you are connecting to the internet behind a proxy, there might be problem in running the commands `easy_install pip` and 
`pip install django`. Set the environment variables for proxy configuration in the command prompt as follows:

`set http_proxy=http://username:password@proxyserver:proxyport`
`set https_proxy=https://username:password@proxyserver:proxyport`
