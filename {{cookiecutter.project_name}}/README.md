# ds-fastapi-template
Add top level description to your project. Should not exceed 500 words.  
Also add helpful links to internal documentation if available. 

# Working in this Repo 

## Install dependencies

`$ pip install -r requirements.txt`  
`$ pip install -r requirements_dev.txt`
## Running in Docker container

`$ docker-compose up`  
After the image is built and the container has started you can start interacting with it, unless you have configured the ports differently it should be reachable under `http://localhost:8000/`

## Access OpenAPI/Swagger Interface

See `http://localhost:8000/docs`

## Interacting with the API-Endpoints

Specify the main routers that should be used, highlight other routers that may be helpful. (e.g. health router)  

## Configuring the service
If the service is configurable in any way, please provide descriptions of options and value ranges etc.  

## Testing
Provide info on how to mock data or requests for test purposes and add expected results to it.  
This may also link to a report page which shows results of automated testing.


