<H1>Gists Service Test Automation Project</H1>

<H2>About this project</H2>
<p>This project was created for practicing building webservice in python using microservices architecture methodologies and best practices.</p>

<H2>Deploying Lists-Service</H2>
<h3>Prerequisites</h3>
Docker Daemon installed on your system

<h3>Steps</h3>
1. Clone this repository to a local folder<br><br>
2. From the repository root folder type in terminal:
<br> `docker-compose up -d --build lists-service`

<h3>Endpoints</h3>
<h4>Base Endpoint: </h4>
`http://localhost:5000`
<h4>GET :</h4> `/lists` <br>_return all lists_<br><br> `/lists/:list-id` <br> _return a list by its id_
<br><br> `/lists?xml=true` <br>
_return all lists as xml_
<br><br> `/lists/:list-id?xml=true`
<br>_return a list by its id as xml_
<h4>POST :</h4> `/lists`<br>_create new list_
<h5>Request Payload:</h5> `{
    "listName": "example list",
    "listType": "shopping"
}`

<h5>Response Payload:</h5> `{
  "listID": id
}`
<h4>PUT :</h4> `/lists/:list-id`<br>_update existing list_
<h5>Request Payload:</h5> `{
    "listName": "example list new name",
    "listType": "other type"
}`

<h4>PATCH :</h4> `/lists/:list-id/items`<br>_update items in existing list_
<h4>DELETE :</h4> `/lists/:list-id` <br>_delete existing list_


<h4>Created By:</h4>
<H5>_Ran Markovich_</H5>
