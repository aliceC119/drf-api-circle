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

















------

