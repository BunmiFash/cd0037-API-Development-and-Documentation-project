# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`


                                API DOCUMENTATION
 INTRODUCTION: The Trivia API is a Restful API, hence follows all REST principles. With this API, users are able to add questons,delete questions,search questions and retrieve questions as well as the category each question belongs.

 GETTING STARTED:
        BASE URL: This API is hosted on localhost 127.0.0.1 and on port 5000, hence can be accessed via http://127.0.0.1/5000

RESOURCES ENDPOINT: The folLowing are the endpoints allowed by the Trivia API and the resources accessed.

   1. Endpoint: /categories
      Method: GET
      Resource: This will retrieve all the categories present in the API.
      curl example: curl -X GET http://127.0.0.1/5000/categories
      This will return:
      "categories": {
          "1": "Science",
          "2": "Art",
          "3": "Geography",
          "4": "History",
          "5": "Entertainment",
          "6": "Sports"
       },
  "num_of_categories": 6,
  "success": true
}

   2.Endpoint: /questions?page=1
      Method: GET
      Resource: This will retrieve all the questions present in the page 1 as well as all the categories and total number of questions in the API.
      curl example: curl -X GET http://127.0.0.1/5000/questions?page=1.
      response:
               "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory":"History",
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "totalQuestions": 23
}

3. Endpoint: /questions/24
   Method: DELETE
   Response: This endpoint will delete question with id of 24 and will return the remaining questions.
   curl example:  curl -X DELETE http://127.0.0.1:5000/questions/24

   "deleted_question": 24,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "totalQuestions": 22
}

    4. Endpoint: /questions
       Method: POST
       Response: This endpoint adds a new question and answer as well as the category and difficulty of the new question. It returns succcess as true if the question is added sucessfully.
       curl: curl -X POST -H "Content-Type:application/json" -d '{"question":"When did Nigeria gain Independence?", "answer":"October 1st, 1960", "difficulty":"3", "category":"1"}' http://127.0.0.1:5000/questions
          
            {
      "success": true
    }

4. Endpoint: /questions/search
     Method: POST
     Response: It returns questions with the searched keyword.
     curl : curl -X POST -H "Content-Type:application/json" -d '{"SearchTerm":"Who"}'http://127.0.0.1/5000/questions/search
       "currentCategory": "History",
    "questions": [
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "there",
      "category": 3,
      "difficulty": 2,
      "id": 24,
      "question": "who is"
    },
    {
      "answer": "there",
      "category": 3,
      "difficulty": 2,
      "id": 25,
      "question": "who is"
    }
  ],
  "success": true,
  "totalQuestions": 4
}

5. Endpoint: /questions/create
   Method: POST
   Resource: This endpoint adds a new question and answer as well as the category and difficulty level.

   curl example: curl -X POST -H "Content-Type:application/json" -d '{"question":"When did Nigeria gain independence?", "answer":"October 16, 1960","difficulty":"2","category":"4"}' http://127.0.0.1:5000/questions/create
      {
  "success": true
}

 6. Endpoint: /categories/3/questions
    Methods: GET
    Resources: This endpoint retrieves a set of questions based on the category they belong to oe questions in the same category are returned.
    curl example: curl http://127.0.0.1:5000/categories/3/questions
    
          "currentCategory": "Geography",
          "questions": [
            {
              "answer": "Lake Victoria",
              "category": 3,
              "difficulty": 2,
              "id": 13,
              "question": "What is the largest lake in Africa?"
            },
            {
              "answer": "The Palace of Versailles",
              "category": 3,
              "difficulty": 3,
              "id": 14,
              "question": "In which royal palace would you find the Hall of Mirrors?"
            }
          ],
          "success": true,
          "totalQuestions": 2
        }
          
    ERROR HANDLING
    The following errors are captured is this API.
    Error 400: handles bad requests. For axample deleting a non_existent or alreday deleted question
        def bad_request(error):
             return jsonify({
            'success': False,
            'error': 400,
            'message':"Bad Request'
        }), 400

    Error 404:This error is thrown when a question or category not present is accessed.
           def not_found(error):
                return jsonify({
            'success': False,
            'message':'Resource Not Found',
            'error':404,
         }), 404    

    Error 405: This error is thron when the wrong method is used to access an endpoint.
            def method_not_allowed(error):
                return jsonify({
                    'success': False,
                    'message':'The method is not allowed for the requested URL.',
                    'error': 405
                }), 405  

    Error 422:
            def unprocessable(error):
                return jsonify({
                    'success': False,
                    'message':'The request was well-formed but was unable to be followed due to semantic errors.',
                    'error': 422
                }), 422  

    Error 500:
          def method_not_allowed(error):
              return jsonify({
                  'success': False,
                  'message':'Internal server error.',
                  'error': 500
              }), 500                          