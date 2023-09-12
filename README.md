## INTRODUCTIONS

This API controls a person resource. You can perform complete CRUD on a person instance. To run the app, please follow the instructions below:

- Fork the project to your github and clone the app to your local machine.
- Create and enter a development environment of your choice.
- Install the required dependencies/packages from the 'requirements.txt' file included in the project.
- Run 'python app.py' via the terminal to start the app.

## END-POINTS

# User Create

- default url '/api'
  - Use this endpoint to create a new person instance.
  - send request via 'POST' method
  - Request -> 
        data should be a json object 'attributes' that has all the attributes for the person instance to be created. example

            {
                "attributes": {
                    "name": "Chao",
                    "occupation": "Teacher"
                }
            }
  - Response -> 
        * 200 Person created successfully
        * 400 Bad Request

# Retrieve User

- default url '/api/user_id'
  - Use this endpoint to view a person instance.
  - send request via 'GET' method
  - Response -> 
        * 200 Person object
        * 404 Person not found

# Edit User

- default url '/api/user_id'
  - Use this endpoint to edit a person instance.
  - send request via 'PUT' method
  - Request -> 
            {
                "attributes": {
                    "key": "value",
                }
            }
  - Response -> 
        * 200 Update Success
        * 400 Attributes not provided
        * 404 Person not found

# Delete User

- default url '/api/user_id'
  - Use this endpoint to delete a person instance.
  - send request via 'DELETE' method
  - Response -> 
        * 200 Delete Successful
        * 404 Person not found

