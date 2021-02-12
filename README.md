<H1>Lists Service Test Automation Project</H1>

<H2>About this project</H2>
<p>This project was created for practicing building webservice in python using microservices architecture methodologies and best practices.</p>

<H2>Deploying Lists-Service</H2>
<h3>Prerequisites</h3>
Docker Deamon installed on your system

<h3>Steps</h3>
1. Clone this repository to a local folder<br><br>
2. From the repository root folder type in terminal:
<br> `docker-compose up -d --build lists-service`

<h3>Endpoints</h3>
<h4>Base Endpoint: </h4>
`http://localhost:5000`
<h4>GET :</h4> `/lists` <br> `/lists/:list-id` <br> `/lists?xml=true` <br> `/lists/:list-id?xml=true`
<h4>POST :</h4> `/lists`
<h4>PUT :</h4> `/lists/:list-id`
<h4>PATCH :</h4> `/lists/:list-id/items`
<h4>DELETE :</h4> `/lists/:list-id` 


<h4>Created By:</h4>
<H5>Ran Markovich</H5>
