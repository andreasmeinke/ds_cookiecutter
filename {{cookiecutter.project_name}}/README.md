# ds-fastapi-template
Add top level description to your project.  

# Working in this Repo 

## Install dependencies

`$ pip install -r requirements.txt`  
`$ pip install -r requirements_dev.txt`
## Running in Docker container

`$ docker-compose up`

## Access OpenAPI Interface

See `http://localhost:8000/docs`

## Interacting with the API-Endpoints

Specify the main routers that should be used, highlight other routers that may be helpful. (e.g. health router)  

## Adding the API Template to your local project

`$ git subtree add --prefix <target-folder> <repo-url> <branch-name> --squash`  
This command will copy the specified branch from the repo under the given URL into your local target folder.  
If you change files of the subtree within your local project you can safely commit and push them, they won't change 
the branch from which you have created the subtree in the first place.  
However, if you wish to contribute back to the subtree origin follow the steps here https://www.atlassian.com/git/tutorials/git-subtree#:~:text=surround%C2%A0main%C2%A0%2D%2Dsquash-,Contributing,-back%20upstream
