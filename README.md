### Objective

Your assignment is to implement a bookstore REST API using Python and Django.

### Brief

Lohgarra, a Wookie from Kashyyyk, has a great idea. She wants to build a marketplace that allows her and her friends to
self-publish their adventures and sell them online to other Wookies. The profits would then be collected and donated to purchase
medical supplies for an impoverished Ewok settlement.

### Tasks

-   Implement assignment using:
    -   Language: **Python**
    -   Framework: **Django**
-   Implement a REST API returning JSON or XML based on the `Content-Type` header
-   Implement a custom user model with a "author pseudonym" field
-   Implement a book model. Each book should have a title, description, author (your custom user model), cover image and price
    -   Choose the data type for each field that makes the most sense
-   Provide an endpoint to authenticate with the API using username, password and return a JWT
-   Implement REST endpoints for the `/books` resource
    -   No authentication required
    -   Allows only GET (List/Detail) operations
    -   Make the List resource searchable with query parameters
-   Provide REST resources for the authenticated user
    -   Implement the typical CRUD operations for this resource
    -   Implement an endpoint to unpublish a book (DELETE)
-   Implement API tests for all endpoints

### Evaluation Criteria

-   **Python** best practices
-   If you are using a framework make sure best practices are followed for models, configuration and tests
-   Write API tests for all implemented endpoints
-   Make sure that users may only unpublish their own books
-   Bonus: Make sure the user _Darth Vader_ is unable to publish his work on Wookie Books

### CodeSubmit

Please organize, design, test and document your code as if it were
going into production - then push your changes to the master branch. After you have pushed your code, you may submit the assignment on the assignment page.

All the best and happy coding,

The Vitolus GmbH Team


### Developer notes
-   Install Docker Application from official documentation and run it
    ```
        https://docs.docker.com/desktop/install/mac-install/
    ```
-   Run the following commands while initial setup
    ```
        docker-compose up
        ./manage.py initadmin
    ```
-   If you are not using remote container in VSCode are Pycharm, you can access the remote terminal to run ./manage.py cmds by running
    ```
        docker exec -it <container name> bash
    ```
-   To check the conatainer name
    ```
        docker ps
    ```
-   To login to superadmin
    ``` 
        http://0.0.0.0:8000/admin/
        email: root@gmail.com
        pwd: root1234
    ```
-   Provide an endpoint to authenticate with the API using username, password and return a JWT
    ``` 
        Post call To get Access Token and Refesh Token
        http://0.0.0.0:8000/token/
        Form data
            email: root@gmail.com
            pwd: root1234
        Response: {
            "refresh": <refreshtoken>
            "access": <access_token>
        }
    ```
    ``` 
        Post call To get Access Token From Refesh Token
        http://0.0.0.0:8000/token/refresh/
        Form data
            refresh: <refreshtoken>
        Response: {
            "refresh": <refresh_token>
            "access": <access_token>
        }
    ```
-   Implement REST endpoints for the `/books` resource
    -   No authentication required
    -   Allows only GET (List/Detail) operations
    -   Make the List resource searchable with query parameters
    ```
        Get api for listing books
        http://0.0.0.0:8000/book/
        query parameters
        search=<string> (will check title matches)
        limit=<number> (if given then displays paginated data)
        authentication: not required only for get call
    ```

-   To get data in xml format
    -   curl --location --request GET '0.0.0.0:8000/api/book/' --header 'Accept: application/xml'
-   To get data in json format
    -  curl --location --request GET '0.0.0.0:8000/api/book/' --header 'Accept: application/json'

 -   Provide REST resources for the authenticated user
    -   Implement the typical CRUD operations for this resource
    -   Implement an endpoint to unpublish a book (DELETE)