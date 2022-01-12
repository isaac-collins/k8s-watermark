# k8s-watermark

Simple web application that manipulates a user's uploaded image by adding a text watermark
and saves the image to a database:

## backend

Flask app that uses OpenCV library to apply text to user's uploaded image
1. Receive JSON from `frontend` containing Base64 encoded image and user text
1. Convert b64 to OpenCV image array, apply user text, convert back to b64
1. Send b64 encoded image back to `frontend` and post image data to `db-api`

## db-api

Flask-RESTful app that exposes a REST API for the other services to interact with the Images database

* Routes
    * **GET** `/images` Returns all Image objects from Images database
    * **POST** `/images` Creates new Image object from request body and inserts into Images database
    * **GET** `/images/<int:image_id>` Returns Image objects by image ID
    
## frontend 

HTML\Javascript served by NGINX 
