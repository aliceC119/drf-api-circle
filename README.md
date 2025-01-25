# The drf-api-circle

## Advanced Front-End Portfolia Project(PP5) 

The drf-api-circle is the backend for the Circle application, developed using the Django Rest Framework (DRF). It serves as the foundation for a social network (Circle) dedicated to sharing ideas about classical music, specifically designed for classical music enthusiasts.

The drf-api-circle is designed for users to share their favourite musicians through pictures and videos. Users can like, comment on and copy posts or videos, which encourages communication within the platform. To enhance the user experience, the backend application also includes a follow function that allows users to follow or unfollow each other. 

This API is built to integrate smoothly with a React frontend, ensuring a seamless experience for users who want to connect and engage with each other.

## Key Apps


posts: Create/delete posts or video posts

profiles: Handles user profiles and related information.

comments: Enables users to comment on a post or a video post.

likes: Allows users to like a Post or a Video Post they are interested in.

followers: Allows users to follow and track the activities of other users.



------
### Table of Contents

## User Experience 

I planned this project using an Agile methodology. The implementation was carried out through the GitHub Project board, where I organized the user stories

## User stories

| Id | User Story | Implemented |
| -- | ---------- | ----------- |
| 1  | As a developer I can set up the base setting for the api backend so that I can build up the features for this project | Done |
| 2  | As a superuser I can create an account in the backend so that I can manage all activities in the backend environment| Done |
| 3  | As a superuser I can update my profile with the info of name, profile picture so that my account can be personalized| Done |
| 4  | As a developer I will create an App 'profiles' so that the superuser can update their info in the profile page | Done |
| 5  | As a developer I will create and App 'posts so that the superuser can create a post with pictures and YouTube videos, and check the posts list and video post list| Done |
| 6  | As a developer I will create and App 'likes' so that the superuser can like a post or a video post, and check the list of the liked posts and video posts | Done |
| 7  | As a developer I will create an App 'comments' so that the superuser can comment on a post or a video post, and to check the comment list. | Done |
| 8  | As a developer I will create an App 'followers' so that the superuser can follow other users, and to check the list of followers| Done |



## Structure

The database schema was created using [dbdiagramm](https://dbdiagram.io/home) 

![dbdiagram(api)](https://github.com/user-attachments/assets/2604f041-40c8-4b1b-b094-d90367c53589)

## Database

A PostgresSQL provided by Code Institute was used for this project.

+ FieldTypes:
    - AutoField: An integer field that automatically increments.
    - CharField: A text field to store large text.
    - DateTimeField: A field to store data.
    - ForeignKey: A field to link data in one table to the data in another table, it is a many-to-one relationship.
    - TextField: A field to store text entries.
    - URL: A CharField for URL.
    - Image: A FileDield with uploads restricted to image formats only.
    - OneToOneField: A Field for a one-to-one relationship.
  
## API Endpoints

The endpoints provided by the API are as below:

| Endpoint | HTTP Method | CRUD Operation |
| -------- | ----------- | -------------- |
| /dj-rest-auth/registration/ | POST | N/A |
| /dj-rest-auth/login/ | POST | N/A |
| /dj-rest-auth/logout/ | POST | N/A |
| /profiles/ | GET | Read|
| /profiles/<int:pk>/ | GET | Read|
|  | PUT | Update |
| /posts/ | GET | Read|
|  | POST | Create|
| /posts/<int:pk>/ | GET | Read|
|  | PUT | Update |
|  | DELETE | Delete |
| /video-posts/ | GET | Read|
| /video-posts/<int:pk>/| GET | Read|
|  | PUT | Update |
|  | DELETE | Delete |
| /comments/posts/ | GET | Read|
|  | POST | Create|
| /comments/posts/<int:pk>/ | GET | Read|
|  | PUT | Update |
|  | DELETE | Delete |
| /comments/video-posts/ | GET | Read|
|  | POST | Create|
| /comments/video-posts/<int:pk>/ | GET | Read|
|  | PUT | Update |
|  | DELETE | Delete |
| /likes/posts/ | GET | Read|
|  | POST | Create|
| /likes/posts/<int:pk>/ | GET | Read|
|  | DELETE | Delete |
| /likes/videoposts/ | GET | Read|
|  | POST | Create|
| /likes/videoposts/<int:pk>/ | GET | Read|
|  | DELETE | Delete |
| /followers/ | GET | Read|
|  | POST | Create|
| /followers/<int:pk>/ | GET | Read|
|  | DELETE | Delete |

## Technologies Used 
### Language:
+ Python
  
### Frameworks:
+ [Django Rest Framework](https://www.django-rest-framework.org/)
+ [Django](https://www.djangoproject.com/)

### Libraries
+ os: An Operating System is a System software that manages all the resources of the computing deice.
+ [Gunicon](https://gunicorn.org/):  The Gunicorn "Green Unicorn" (pronounced jee-unicorn or gun-i-corn)[2] is a Python Web Server Gateway Interface (WSGI) HTTP server.
+ [Pycopg 2](https://pypi.org/project/psycopg2/): Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
+ [dj_database_url](https://pypi.org/project/dj-database-url/): A method returns a Django database connection
dictionary, populated with all the data specified in the URL.
+ [asgiref 3](https://pypi.org/project/asgiref/): a standard for Python asynchronous web apps and servers to communicate with each other.
+ [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/#:~:text=Django%20Cloudinary%20Storage%20is%20a,both%20media%20and%20static%20files.): a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
+ [django-cors-headers](https://pypi.org/project/django-cors-headers/#:~:text=django%2Dcors%2Dheaders%20is%20a,Origin%20Resource%20Sharing%20(CORS).) :a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
+ [django-filter](https://django-filter.readthedocs.io/en/stable/): The filter() method is used to filter search.
+ [oauthlib](https://pypi.org/project/oauthlib/#:~:text=OAuthLib%20is%20a%20framework%20which,onto%20your%20favourite%20web%20framework.): a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
+ [pillow](https://pypi.org/project/pillow/): for image processing.
+ [PyJWT](https://pypi.org/project/PyJWT/): allows you to encode and decode JSON Web Tokens (JWT).
+ [python3-openid](https://pypi.org/project/python3-openid/#:~:text=This%20is%20a%20set%20of,consumer%20package.): support the use of the OpenID decentralized identity system in your application, update to Python 3. Want to enable single sign-on for your web site? Use the openid.consumer package.
+ [pytz](https://pypi.org/project/pytz/) : a functionality that allows you to work with time zones in a Python application.
+ [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) : provide an easy-to-use Python interface for building OAuth1 and OAuth2 clients.
+ [sqlparse](https://pypi.org/project/sqlparse/) :a non-validating SQL parser for Python.


### Tools:
+ [GitHub](https://github.com/)
+ [CI Gitpod](https://codeinstitute-ide.net/workspaces)
+ [Heroku](https://www.heroku.com/)
+ [Cloudinary](https://cloudinary.com/)
+ [Canva](https://www.canva.com/en_gb/)

------

## Deployment 

### Heroku 
The application is deployed on Heroku via a GitHub connection. To deploy a Heroku project, below are the steps I used.
In Heroku, this is configured under Config Vars in the Settings tab.

## Step 1: Create an App on Heroku

Log in to your Heroku dashboard with your username and password, and confirm the access code with the two-factor verification app of your choice.

Login to Heroku

<img width="917" alt="Screenshot 2025-01-25 at 20 24 52" src="https://github.com/user-attachments/assets/fd82609c-d398-4251-9844-51ca3e783f64" />

Verify your identity by entering the verification code generated by an authenticator

<img width="918" alt="Screenshot 2025-01-25 at 20 26 20" src="https://github.com/user-attachments/assets/a8602e35-8262-4749-b751-ff7598b3a272" />

Create a new Heroku app

<img width="188" alt="Screenshot 2025-01-25 at 20 28 21" src="https://github.com/user-attachments/assets/c7c63ad3-7e57-4a00-b842-39431dcaab1b" />

## Step 2: Connect to GitHub
Once a new app is created, go to `Deploy` in the top toolbar, then select the GitHub box in the middle to connect this Heroku app to a GitHub repository.

<img width="1486" alt="Screenshot 2025-01-25 at 20 34 01" src="https://github.com/user-attachments/assets/500b5f17-a65b-4726-ad6a-1075bdf36f19" />

## Step 3: Deploy your app

Choose `main` as the branch to deploy and click on 'Deploy Branch'. You can do the deploment actomatically or manuelly at this point.

## Step 4: View the application

The app can be found by clicking the 'Open App' button in the top right corner with the Heroku URL configuration as follows: https://*.herokuapp.com

<img width="1479" alt="Screenshot 2025-01-25 at 20 36 32" src="https://github.com/user-attachments/assets/98e1505d-fc1d-4903-88bd-e2d558124e80" />

## Step 5: 

Go back to the workspace and add the Heroku app URL in this format "https://*.herokuapp.com" in the settings.py into CSRF_TRUSTED_ORIGINS.
<img width="333" alt="Screenshot 2025-01-25 at 21 03 02" src="https://github.com/user-attachments/assets/16d40ed6-b59d-4ab6-ad86-e09ac16433c9" />

### Cloudinary 

Go to [Cloudinary](https://cloudinary.com/) and sign up to open an account

<img width="633" alt="Screenshot 2025-01-25 at 20 38 58" src="https://github.com/user-attachments/assets/92b99d62-1571-4ff6-811d-2fe63af6dee1" />

## Step 2:
Go to `Getting Started` in the option column. Copy the CLOUDINARY_URL in inside `View API Keys`.

<img width="820" alt="Screenshot 2025-01-25 at 20 39 04" src="https://github.com/user-attachments/assets/5d19e94c-2806-42e8-bea2-7b19a4977c08" />

## Step 3:
Connecting your project to Cloudinary by placing the CLOUDINARY_URL in the env.py file in your workspace.

<img width="798" alt="Screenshot 2025-01-25 at 20 43 27" src="https://github.com/user-attachments/assets/765e32fb-f776-482f-bf32-7526a363876b" />

## Step 4:
Open the settings.py file and add the apps to `INSTALLED_APPS`.

<img width="288" alt="Screenshot 2025-01-25 at 20 43 13" src="https://github.com/user-attachments/assets/a621f781-c8a0-41e5-a55b-03558d0e04b7" />

## Step 5: 

Return to the Heroko dashboard, and click the Settings tab and the Reveal config vars button. Add a CLOUDINARY_URL key:value pair. Copy the value from the env.py file.

<img width="1308" alt="Screenshot 2025-01-25 at 20 50 19" src="https://github.com/user-attachments/assets/8b750cbe-a380-45aa-b23c-1322af6cc04b" />

## Step 6: 

Click on the Deploy tab, scroll down, choose the main branch and press Deploy Branch.


<img width="571" alt="Screenshot 2025-01-25 at 20 53 55" src="https://github.com/user-attachments/assets/68a12e66-c7f9-4d85-9821-1d59bef332db" />

## Step 7: 

Go back to the workspace and add CLOUDINARY_URL into os. 

<img width="586" alt="Screenshot 2025-01-25 at 20 57 38" src="https://github.com/user-attachments/assets/6ebf4b7f-9a9f-4085-b238-8125fddf1d3b" />

## Credits 












