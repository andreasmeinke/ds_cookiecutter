# ds-fastapi-template
Template for DS Projects using FastAPI.  

## Install dependencies

`$ pip install -r requirements.txt`

## Running in Docker container

`$ docker-compose up`

## Access OpenAPI Interface

See `http://localhost:8000/docs`

## Interacting with the API-Endpoints

Send a GET-Request to http://localhost:8000/entities via tooling of your choice (e.g. Postman)  
The body of the request has to be a JSON with a key "text" with a String value.  
You can also specify model size and model language via corresponding key's and value's.

## Adding the API Template to your local project

`$ git subtree add --prefix <target-folder> <repo-url> <branch-name> --squash`  
This command will copy the specified branch from the repo under the given URL into your local target folder.  
If you change files of the subtree within your local project you can safely commit and push them, they won't change 
the branch from which you have created the subtree in the first place.  
However, if you wish to contribute back to the subtree origin follow the steps here https://www.atlassian.com/git/tutorials/git-subtree#:~:text=surround%C2%A0main%C2%A0%2D%2Dsquash-,Contributing,-back%20upstream
