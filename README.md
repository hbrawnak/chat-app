## Chat server

Chat Application allows users to group messaging. Application confirms the data persistence and real time messages pop up to the other users end. Python is used to build the application and Socket for real time. Data is stored in MongoDB asynchronously by RQ package.


Installation:

Docker should be pre-installed. Clone the chat-app repository and move inside the folder. 

~~~~
Step 1: Create an environment file (.env) from .env.test

Step 2: Run `docker build -t chat-app .` 

Step 3: Run `docker-compose up` 
~~~~
Now the application should run on 127.0.0.1:5000. 
