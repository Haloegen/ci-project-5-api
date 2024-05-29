# Re.view
## **Project Overview**

RE.view is a product review app, where users can share experiences with products and give their opinions on other products. 

The RE.view API is the back-end portion of the RE.view app and has been developed using Django's Rest Framework. The app aims to let users share product reviews, and let users like or dislike them, leave their own review and follow their favourite reviewers on the website. The API attempts to create a smooth and enjoyable user experience, by providing the front end with its core functionality and logic.

To view the deployed API, [*_click this link_*](https://review-app-drf-b1e1686b7d68.herokuapp.com/)

This is the backend repository for this project. To go the front end repository, [*_click this link_*](https://github.com/Haloegen/re.view-ci)

To view the deployed RE.view front-end app, [*_click this link_*](https://re-view-198da65eeda5.herokuapp.com/)

## **Table of Contents:**

1. [**Project Overview**](#project-overview)
1. [**Project Planning**](#project-planning)
   - [**Project Aims (API)**](#project-aims-api)
   - [**User Stories**](#user-stories)
1. [**Database Schema**](#database-schema)
   - [**Data Models**](#data-models)
   - [**API Endpoints**](#api-endpoints)
1. [**Technologies Used**](#technologies-used)
1. [**Testing**](#testing)
1. [**Deployment**](#deployment)
1. [**Credits**](#credits)
   - [**Honourable Mentions**](#honourable-mentions)
   - [**Code and Content References**](#code-and-content-references)


## **Project Planning**

### **Project Aims (API):**

- To provide the front-end app with a robust back-end counterpart that allows communication between React/JavaScript and Python.
- To implement user authorisation through the use of Django AllAuth and Django Rest Auth, allowing users to create accounts, login and logout on the front-end
- To provide CRUD functionality to users on the front-end in relation to posts and comments:
  - Logged in users can create, edit and delete their own posts.
  - Logged in users can create, edit and delete their own comments.
  - Logged in users can choose one of two reactions to any post that is not their own, and they can change or undo these reactions at will.
  - Logged in users can like any product review that is not their own, and unlike it at will, and also dislike a project at will.
- To provide CRUD functionality to users on the front-end in relation to their profiles and following other profiles:
  - Logged in users can edit their own profile by uploading a profile image and amending their profile's content whenever they wish.
  - Logged in users can follow the profiles of other users, and unfollow at will.
- To provide the front-end with a number of options that allow logged in users to control the product reviews they see, by applying filters (such as reviews by only showing reviews by users they follow, or viewing the reviews they have liked) or using the search bar to search for reviews that use specific keywords, or are by specific profiles.
- To allow logged out users to view reviews.

### **Data Models**

#### **User** 
- The user model is provided by DjangoAllauth, and enableds users to create an account with a username and passwordm, and assigning each profile a unique foreign key

#### **Profile**
- The profile model creates a new user profile whenever a new instance of the User model is created. this is possible thanks to the 'Create_profile' function. Once created,users are able to update their profile name, content, and profile image.

#### **Follower**
The Follower model allows logged in Users to follow of unfollow other users on the front-end. A 'follow' equals the creation of a new Follower isntance, whereas an 'unfollow' deletes that instance for the database. A user can only have on unique follower Id per user followeed, preventing users from being able to follow the same person multiple times.

#### **Products**
- The product model centres around the fundamental CRUD functionality that users can create, read, edit/update and delete (this is only possible for the post creator)
- The Product has two custom components being the unlike/dislike(in hind sight I should have changed the naming of this, but as the project is finished it is abit late in the development cycle to fix, in future explanations I shall try to clarify between the ability to unlike a product you have liked, and disliking a project you have disliked).
The other custom model is the review model, which uses similar code to the comment section in the Django+React project walkthrough.

- We added a custom field being the price and the link models, which will allow users to share where they purchased the good via a link, and the price they paid for such goods.
- In the future an better implentation would be the use of multiple content fields to help users expand on the product using multiple choices to help other users understand where the product fell short

#### **Reviews** 
The review model is a custom model that replaces the comments model from the walkthrough, this is a review of the product that a user has submitted.
- Users can submit and edit reviews and this also has a unique together field which makes each product, have its unique id tied to the reviews.


#### **Likes** 
The like model is the users ability to have increased interaction with a product and display their appreciation with a visual aid being the thumbs up(likes_count)
- The like_id is attached to the user when they like a product, and its unique which helps prevents duplicates(at the time of writing this, their is a bug, where a user can spam the input and break the page on client side, which is fixed when the user refresh's, an additional future implentation could be validation to prevent this being an issue)

#### **Unlikes** 
The unlike model functions similarly to the like function, this is essentially the dislike button, not the ability to unlike something you have liked
- the unlike_id is generated the same was as the like_id, similar with the Unlike_count

#### **Pagination**
The review API uses pagination which is currently set to the global limit is 10. I have used Infinite scroll, which allows reviews and products to be loaded beyond the limit

## **Technologies Used**

The language used to write this API is Python. Below is a list of the frameworks and libraries used to create this project, as well as other dependencies:

- Django - the Python framework used to develop this project.
- Django REST Framework - the Django toolkit that enabled the creation of this API.
- Django AllAuth - enabling user authentication and validation.
- Django Rest Auth - to provide endpoints for users to login/logout.
- CodeInstitute SQL - to host the PostgresSQL database used by this project.
- Psychopg2 - a database adaptor that enables interaction between Python and PostgresSQL.
- Cloudinary - to host images and static files that engage seamlessly with the front- and back-end counterparts of this project.
- Pillow - an imaging library that adds image processing capabilities.
- Django Filters - to allow queryset filtering based on model fields.
- Django CORS Headers - to handle the server headers required for Cross-Origin Resource Sharing.
- Heroku - providing a platform in which to host the deployed project.

## **Testing**
this is handled in a separate readme

## **Deployment**
In this part I will explain how I deployed this project, so that other users can clone and work on it

#### **Cloning/Forking**
If you wish to create a clone of this project to use on your local machine or Virtual IDE, first navigate to [this projects repository](https://github.com/Haloegen/ci-project-5-api)
then in the local terminal run this command
'pip install -r requirement.txt' 
this will install all the required libraries and packages.

#### **Project Setup**

below is a list of the steps to install the necessary packages and libraries for this project.
1. Create a virtual environment/or use a base gitpod repo(if this is the case please skip to where the packages are installed):
   - `python3 -m venv [your_venv_name]`
   - IMPORTANT: Add the .env file to .gitignore so that it is not tracked with version control.
1. Open the virtual environment and install Django with Gunicorn:
   - `source [your_venv_name]/bin/activate`
   - `pip install django gunicorn`
1. Install the following supporting libraries:
   - `pip install django-cloudinary-storage==0.3.0`
   - `pip install dj-database-url==0.5.0 psychopg2-binary`
   - `pip install Pillow==9.3.0`
1. Create a requirements.txt file:
   - `pip3 freeze --local > requirements.txt`
1. Create your Django project:
   - `django-admin startproject project_name .` (note: 'project_name' in this case is 'creature_feature_api' - do not forget the `.` after the project name.)
1. Create apps within the project:
   - `python3 manage.py startapp app_name` (note: 'app_name' references the name of the app, and in the case of this project there are several. A separate app should be created for each major aspect of the project, so the apps created for this project are 'reviews', 'followers', 'likes','unlikes', 'products' and 'profiles'.)
1. In `settings.py`, which is created in the main project directory, add the newly created app(s) to the bottom of the `INSTALLED_APPS` list.
1. Run the following commands to make migrations, and then migrate the changes:
   - `python3 manage.py makemigrations`
   - `python3 manage.py migrate`
1. To test that everything has been set up correctly, run the server locally:
   - `python3 manage.py runserver` (note: you may need to adjust the `ALLOWED_HOSTS` section of `settings.py` if Django provides an error stating so.)


#### **Database Setup**
This project uses [**_Code institute SQL Database_**] to host its database.

Click create an sql, submit email addess and you will recieve an email with the url of the sql database


#### **Django REST and JWTs**

1. Install Django REST Framework:
   - `pip install djangorestframework`
   - Add `rest_framework` to your `INSTALLED_APPS`
1. Install Django Rest Auth:
   - `pip install dj-rest-auth==2.1.9`
1. Install Django Filters:
   - `pip install django-filter`
1. Add the following to `INSTALLED_APPS`:
   - `'django_filters'`, `'rest_framework.authtoken'`, `'dj_rest_auth',`
1. Include the following in the main `urls.py` file:
   - `urlpatterns = [path('api-auth/', include('rest_framework.urls')), path('dj-rest-auth/', include('dj_rest_auth.urls')), path('', include('profiles.urls')),]`
1. Migrate the changes to the database (`python3 manage.py migrate`)
1. Install Django AllAuth:
   - `pip install 'dj-rest-auth[with_social]'`
1. Add the following to `INSTALLED_APPS`:
   - `'django.contrib.sites', 'allauth', 'allauth.account', 'allauth.socialaccount', 'dj_rest_auth.registration',`
1. Below `INSTALLED_APPS`, add the new variable `SITE_ID=1`
1. Update the main `urls.py` file:
   - `urlpatterns = [path('dj-rest-auth/', include('dj_rest_auth.urls')), path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), path('', include('profiles.urls')),]`
1. Install Django REST's Simple JWTs:
   - `pip install djangorestframework-simplejwt==4.7.2`
1. Create a `DEV` environment variable in your `env.py` file:
   - `os.environ['DEV'] = 1`
1. Add the following to `settings.py`:
   - `REST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES': [( 'rest_framework.authentication.SessionAuthentication' if 'DEV' in os.environ else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'  )] }`
   - `REST_USE_JWT = True`
   - `JWT_AUTH_COOKIE = 'my-app-auth'`
   - `JWT_AUTH_SECURE = True`
   - `JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'`
   - `JWT_AUTH_SAMESITE = 'None'`

#### **Adding the root route**

1. Create a `views.py` file in the main project folder (in this case 'creature_feature_api') and add the following:
   - `from rest_framework.decorators import api_view`
   - `from rest_framework.response import Response`
   - `from .settings import (JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE,)`
1. Add the following to the main `urls.py` file:
   - `urlpatterns = [path('', root_route)]`
1. Make sure to update your requirements.txt file (`pip freeze > requirements.txt`)


#### **Deployment to Heroku**

This project is hosted on [**_Heroku_**](https://www.heroku.com/).
1. On the Heroku Dashboard, create a new app. The app name must be unique and should be related to the Django project name.
1. Set location as appropriate.
1. Open the 'Settings' tab and navigate to 'Config Vars' - Click 'Reveal Config Vars'.
1. Add the following config vars:

   - `ALLOWED_HOST` = (your hosted front-end site URL)
   - `DATABASE_URL = postgres://CI-database-Url` (note that this must be the unique  URL from the created database)
   - `SECRET KEY = SecretKey123` (note that this must be the unique secret key made previously for this project)
   - `CLOUDINARY_URL = cloudinary://Cloudinary API URL` (note that this must be the unique Cloudinary API URL obtained previously)
   - `CLIENT_ORIGIN = Your URL LINK` (this must be the link of the deployed front end application)

1. Add the following temporary config var (to be removed before final deployment):
   - `DISABLE_COLLECT_STATIC = 1`
1. Obtain the project URL from Heroku, and add it to the 'ALLOWED_HOSTS' section of `settings.py`
1. Create a Procfile in the root project directory and add the following code:
   - `web: gunicorn project_name.wsgi` (note that 'project_name' must be the same as the Django project)
1. Save all project files, and use the following commands to add, commit and push the changes to the GitHub repository:
   - `git add .`
   - `git commit -m "Initial commit"`
   - `git push`
1. Navigate to the 'Deploy' tab in the Heroku dashboard and link the GitHub repository to the project.
1. Manually deploy from the main GitHub repository branch.

## **Credits**

 Richard Wells 
 - My mentor who helped me process and fix bugs and also provided me with insight and knowledge who helped me complete this project


### Code and Content References

- This project was created by following along with [**_Code Institute_**](https://codeinstitute.net/)'s 'Django REST Framework' course content and walkthrough, and as such will bear significant resemblance to it.