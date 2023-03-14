This is a simple FastAPI application to perform CRUD operation in mysql database and a web_scrapper script to collect details from https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx and store it in MySQL database.
  
**Prerequisite**:  
_docker_  
_docker-compose_
  
**To built the image**:  
_cd ~/sparkcapital-Assignment/src && docker built -t python_image:latest ._
  
**To start the app**:  
_docker-compose up -d_
  
  
**APIs for CRUD:**  
**create**: localhost:5000/create-user/  
**read**: localhost:5000/read-user/{user_id}  
**update**: localhost:5000/update-user/  
**delete**: localhost:5000/delete-user/{user_id}  
