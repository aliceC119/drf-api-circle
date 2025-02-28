# The drf-api-circle



## Advanced Front-End Portfolia Project(PP5) 

The drf-api-circle is the backend for the Circle application, developed using the Django Rest Framework (DRF). It serves as the foundation for a social network (Circle) dedicated to sharing ideas about life in general.

The drf-api-circle is designed for users to share their lives through pictures and videos. Users can like, comment on and copy posts or videos, which encourages communication within the platform. To enhance the user experience, the backend application also includes a follow function that allows users to follow or unfollow each other.


This API is built to integrate smoothly with a React frontend, ensuring a seamless experience for users who want to connect and engage with each other.

+ The deployed API is available [here](https://drf-api-circle-320cd30d1665.herokuapp.com/)
+ The GitHub repository for the associated Frontend can be found [here](https://github.com/aliceC119/circle)

## Key Apps


posts: Create/delete posts or video posts

profiles: Handles user profiles and related information.

comments: Enables users to comment on a post or a video post.

likes: Allows users to like a Post or a Video Post they are interested in.

followers: Allows users to follow and track the activities of other users.



------
## Table of Contents

+ [User Experience](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#user-experience)
+ [User stories](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#user-stories)
+ [Structure](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#structure)
+ [Database](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#database)
+ [Models](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#models)
    - [Comments](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#comments)
    - [Followers](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#followers)
    - [Likes](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#likes)
    - [Posts](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#posts)
    - [Profiles](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#profiles)
+ [API Endpoint](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#api-endpoints)
+ [Technologies Used](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#technologies-used)
    - [Language](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#language)
    - [Frameworks](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#frameworks)
    - [Libraries](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#libraries)
    - [Tools](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#tools)
+ [Testing](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#testing)
    - [Manual Test](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#manual-test)
      
+ [Deployment](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#deployment)
    - [Heroku](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#heroku)
    - [Cloudinary](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#cloudinary)
+ [Credits](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#credits)
    - [Code references](https://github.com/aliceC119/drf-api-circle?tab=readme-ov-file#code-references)
+ [Acknowledgements](https://github.com/aliceC119/drf-api-circle/edit/main/README.md#acknowledgements)

## User Experience 

I planned this project using an Agile methodology. The implementation was carried out through the GitHub Project board, where I organized the user stories

## User stories

| Id | User Story | Implemented |
| -- | ---------- | ----------- |
| [#1](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95176935&issue=aliceC119%7Cdrf-api-circle%7C1)  | As a developer I can set up the base setting for the api backend so that I can build up the features for this project | Done |
| [#2](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177140&issue=aliceC119%7Cdrf-api-circle%7C2)  | As a superuser I can create an account in the backend so that I can manage all activities in the backend environment| Done |
| [#3](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177458&issue=aliceC119%7Cdrf-api-circle%7C3)  | As a superuser I can update my profile with the info of name, profile picture so that my account can be personalized| Done |
| [#4](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177691&issue=aliceC119%7Cdrf-api-circle%7C4)  | As a developer I will create an App 'profiles' so that the superuser can update their info in the profile page | Done |
| [#5](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177867&issue=aliceC119%7Cdrf-api-circle%7C5)  | As a developer I will create and App 'posts so that the superuser can create a post with pictures and YouTube videos, and check the posts list and video post list| Done |
| [#6](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177918&issue=aliceC119%7Cdrf-api-circle%7C6)  | As a developer I will create and App 'likes' so that the superuser can like a post or a video post, and check the list of the liked posts and video posts | Done |
| [#7](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177971&issue=aliceC119%7Cdrf-api-circle%7C7)  | As a developer I will create an App 'comments' so that the superuser can comment on a post or a video post, and to check the comment list. | Done |
| [#8](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95177999&issue=aliceC119%7Cdrf-api-circle%7C8)  | As a developer I will create an App 'followers' so that the superuser can follow other users, and to check the list of followers| Done |
| [#9](https://github.com/users/aliceC119/projects/6?pane=issue&itemId=95178558&issue=aliceC119%7Cdrf-api-circle%7C9)  | As a developer I will create a copy link function for posts and video posts so that the user at the Frontend can copy the link of the posts or the video posts and share them to other social platform.| Done |



## Structure

The database schema was created using [dbdiagramm](https://dbdiagram.io/home) 
![dbdiagram(api)](https://github.com/user-attachments/assets/2604f041-40c8-4b1b-b094-d90367c53589)

+ Field Types:

    - AutoField: An integer field that automatically increments.
    - CharField: A text field to store large text.
    - DateTimeField: A field to store data.
    - ForeignKey: A field to link data in one table to the data in another table, it is a many-to-one relationship.
    - TextField: A field to store text entries.
    - URL: A CharField for URL.
    - Image: A FileDield with uploads restricted to image formats only.
    - OneToOneField: A Field for a one-to-one relationship.
      




## Database
+ Student can get Database URL by navigating to[CI Database Makeer](https://dbs.ci-dbs.net/)

## Models

Each model has a unique purpose and collectively supports a variety of application features that enhance the user experience, from user registration to content creation that serves the purpose of social networking.

### Comments:
This model represents comments on posts and video posts made by users. It is linked to the contrib.auth.model (the user) and the Post model.  In addition to the content of the comment, it keeps track of the times when each comment was created and last updated.

### Followers:
This model maintains the follower-following relationships between users. Each following event is also updated and stored.

### Likes:
This model captures the likes that users give to a post or a video post. It is linked to the contrib.auth and post models. It also records the time when each Like event was created.

### Posts:
This model represents the posts and videos created by users. It is related to the contrib.auth model as the owner of the post and video post. It keeps track of the times when each post and video post was created and last updated, as well as the content of the post and video post, including the title, image, YouTube URL, and description.

### Profiles:
This model is related to the contrib.auth model with the information of the users, such as their name and profile image, and it also keeps track of when each user profile was created and last updated. 
  
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
| /comments/videoposts/ | GET | Read|
|  | POST | Create|
| /comments/videoposts/<int:pk>/ | GET | Read|
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
### Language
+ Python
  
### Frameworks
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


### Tools
+ [GitHub](https://github.com/)
+ [CI Gitpod](https://codeinstitute-ide.net/workspaces)
+ [Heroku](https://www.heroku.com/)
+ [Cloudinary](https://cloudinary.com/)
+ [Canva](https://www.canva.com/en_gb/)

## Testing 
  
### Validation Testing
+ Mostly all tests using the CI Python Linter. [CI Python Linter](https://pep8ci.herokuapp.com/#)
+ There are unresolved E501 'line too long' issues in the `settings.py` file.
  
  <img width="1214" alt="pep8" src="https://github.com/user-attachments/assets/33ff1f54-9472-463b-a661-40fa41a8fc06" />

+ There are unresolved E501 'line too long' issue in the `env.py` file.
  
  <img width="1104" alt="env" src="https://github.com/user-attachments/assets/b74fe8be-3ffb-4982-b8a4-8bf1efc2f920" />

+ Due to time constraints, only a limited number of automated tests could be performed.

  <img width="220" alt="Screenshot 2025-02-26 at 08 56 28" src="https://github.com/user-attachments/assets/0ef4a118-26bc-460d-b71a-9b1942943b25" />

  
### Manual Test

**URL Testing**

| Tested | Expected result | Result |
| -------- | ----------- | -------------- |
| Root URL | Show welcome message | Works as expected | 
| /posts/ | Display posts list| Works as expected | 
| /posts/int:pk/ | Display posts detail| Works as expected | 
| /video-posts/| Display video list| Works as expected |
| /video-posts/int:pk/| Display video post detail| Works as expected | 
| /comments/posts/| Display comment list for post| Works as expected | 
| /comments/posts/int:pk/| Display comment detail for post| Works as expected | 
| /comments/videoposts/| Display comment list for video post | Works as expected | 
| /comments/videoposts/int:pk/| Display comment detail for video post| Works as expected | 
| /likes/posts/| Display likes list for post| Works as expected |
| /likes/posts/int:pk/| Display likes detail for post| Works as expected |
| /likes/videoposts/| Display likes list for video post| Works as expected |
| /likes/videoposts/int:pk/| Display likes detail for video post| Works as expected |
| /followers/| Display followers list| Works as expected |
| /followers/int:pk/| Display followers detail| Works as expected |
| /profiles/ | Display profile lists | Works as expected | 
| /profiles/int:pk/ | Display profile detail| Works as expected | 

**CRUD functionality**

| Tested | Create | View | Update | Delete |
| -------- | ----------- | -------------- | -------------- |  -------------- |
| Posts |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark:  |
| Comments |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark:  |
| Likes |  :heavy_check_mark: | :heavy_check_mark: | - |:heavy_check_mark:  |
| Followers |  :heavy_check_mark: | :heavy_check_mark: | - |:heavy_check_mark:  |
| Profiles |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark:  |




## Deployment 

### Heroku 
The application is deployed on Heroku via a GitHub connection. To deploy a Heroku project, below are the steps I used.


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

## Step 6:
A welcome message is displayed when it is successfully deployed.

<img width="534" alt="Screenshot 2025-02-01 at 15 02 18" src="https://github.com/user-attachments/assets/2df79bd9-2f4e-4fc2-9f34-1663b4dbb44f" />


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


------
## Credits 

+ The setup and overall design of this project are based on the "Moments" walkthrough project from the Code Institute. The main components—including profiles, posts, likes, comments, and followers—were derived from the walkthrough project. Additionally, new elements such as video posts and copy links have been added to enhance this project.


### Code references

+ The following websites were used as a source of knowledge:
  + [GeeksforGeeks](https://www.geeksforgeeks.org/)
  + [reddit](https://www.reddit.com/)
  + [stack Overflow](https://stackoverflow.com/)
  + [Google](https://www.google.de/)
  + Slack Community


## Acknowledgements

+ Many thanks to the Student Support team for helping me with this project, especially Rebecca, Sarah, Oisín, and Roman. Their assistance was invaluable; they supported me every time I got stuck and always tried their best to help me resolve issues. Thank you also to my mentor, Gareth, for showing his support.

+ This project is for educational use.





