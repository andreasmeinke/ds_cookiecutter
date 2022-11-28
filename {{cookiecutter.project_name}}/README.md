# ds-fastapi-template
Add top level description to your project. Should not exceed 500 words.  

# Working in this Repo 

## Install dependencies

`$ pip install -r requirements.txt`  
`$ pip install -r requirements_dev.txt`
## Running in Docker container

`$ docker-compose up`  
After the image is built and the container has started you can start interacting with it, unless you have configured the ports differently it should be reachable under localhost:8000.

## Access OpenAPI Interface

See `http://localhost:8000/docs`

## Interacting with the API-Endpoints

Specify the main routers that should be used, highlight other routers that may be helpful. (e.g. health router)  

## Configuring the service
If the service is configurable in any way, please provide descriptions of options and value ranges etc.  

## Testing
Provide info on how to mock data or requests for test purposes and add expected results to it.  
This may also link to a report page which shows results of automated testing.

## Adding the API Template to your local project

`$ git subtree add --prefix <target-folder> <repo-url> <branch-name> --squash`  
This command will copy the specified branch from the repo under the given URL into your local target folder.  
If you change files of the subtree within your local project you can safely commit and push them, they won't change 
the branch from which you have created the subtree in the first place.  
However, if you wish to contribute back to the subtree origin follow the steps here https://www.atlassian.com/git/tutorials/git-subtree#:~:text=surround%C2%A0main%C2%A0%2D%2Dsquash-,Contributing,-back%20upstream
