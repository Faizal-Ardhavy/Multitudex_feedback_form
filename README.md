# Feedback Form App
The Feedback Form App is a FastAPI-based application using SQLAlchemy async to interact with a PostgreSQL database. The application also includes a Vue.js frontend to display collected feedback data.

# Installation
Install Dependencies

Ensure you have installed all required dependencies by running the following command:
```pip install -r requirements.txt```

# Configure Database

After installing dependencies, update the database path configuration in the following locations:

alembic/env.py:
```DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"```

alembic.ini:
```sqlalchemy.url = postgresql+asyncpg://user:password@localhost/dbname```

app/database.py:
```DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"```
# Running the API

Activate your virtual environment and follow these steps to run the API:

Activate your virtual environment
```source venv/bin/activate  # for Linux/Mac```
```venv\Scripts\activate  # for Windows```

Navigate to the application directory
```cd feedback-form```

Run the server using uvicorn
```uvicorn app.main:app --reload```
The API will run at http://localhost:8000. You can access it via a browser or use tools like Postman for API testing.

# Running the Vue.js Frontend Server

To run the Vue.js frontend server, open a new terminal and follow these steps:

Navigate to the frontend directory
```cd frontend```

Install npm dependencies
```npm install```

Run the frontend server
```npm run serve```
The frontend server will run at http://localhost:8080 by default. You can access it via a browser to use the user interface for the Feedback Form application.

# Testing with Postman
Import Postman File

* Import the JSON file located in the postman_test folder into Postman to execute API tests. This file contains a collection of HTTP requests that can be used to test the functionality of the Feedback Form API.
* Open Postman.
* Click on the Import button in the top left corner.
* Select Upload Files and choose the JSON file from the postman_test folder.
* Once imported, you will see a collection of API requests ready to be executed.
* Configure Global Environment Variables
* To ensure proper testing, configure global environment variables name "SCORE" within Postman.
# Run the test
* Ensure that the FastAPI server is running in your development environment.
* Use the imported collection of requests to run tests in Postman.
* Verify that all API requests return expected responses without any unexpected errors.
