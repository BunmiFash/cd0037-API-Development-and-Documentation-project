import os
import unittest
import json
from urllib import response
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from settings import DB_USER, DB_NAME_TEST, DB_PASSWORD


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name =DB_NAME_TEST
        self.database_path = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD,'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.question = {"question":"When did Nigeria gain Independence", "answer":"October 1st, 1960","difficulty":"3","category":"5"}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


    def test_pagination(self):
        response = self.client(self)
        
        self.assertTrue(['current_questions'])

    
    def test_get_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['num_of_categories'])

    def test_wrong_or_non_existent_category(self):
        response = self.client().get('/categories/2')
        data = json.loads(response.data)

        self.assertEqual(response.status_code,404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    def test_get_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['currentCategory']))

    def test_404_get_wrong_question_url(self):
        response = self.client().get('/question')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')        

    def test_delete_questions(self):
        response = self.client().delete('/questions/16')
        data =  json.loads(response.data)
        question = Question.query.filter(Question.id==16).one_or_none()
        # 9,2,4,6,14,16,17,18

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted_question'],16)
        self.assertEqual(question,None)
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['questions']))

    def test_422_delete_questions(self):
        response = self.client().delete('/questions/500')
        data =  json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'The request was well-formed but was unable to be followed due to semantic errors.')

    def test_post_new_question(self):
        response = self.client().post('/questions/create', json =self.question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_new_question_with_wrong_endpoint(self):
        response = self.client().post('/questions/1', json =self.question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'The method is not allowed for the requested URL.')
        
    def test_search_question(self):
        response = self.client().post('/questions/search', json = {'searchTerm':'who'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])    
        self.assertTrue(data['totalQuestions'])
      

    def test_search_non_existent_question(self): 
        response = self.client().post('/questions/search', json = {'searchTerm':'appleterm'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['totalQuestions'],0)    
        self.assertEqual(len(data['questions']), 0)

    def test_questions_by_category(self):
        response = self.client().get('/categories/2/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(len(data['questions']))    
    
    def test_questions_by_wrong_category(self):
        response = self.client().get('/categories/812/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['totalQuestions'],0)
        self.assertEqual(len(data['questions']),0) 

    def test_quiz(self):
        response = self.client().post('/quizzes', json={"previous_questions":[2,4,6,10],"quiz_category":{"id":"2","type":"art"}})
        data = json.loads(response.data)

        self.assertEqual(response.status_code,200) 
        self.assertEqual(data['success'],True)
        self.assertTrue(data['question'])  

    def test_quiz_with_wrong_method(self):
        response = self.client().get('/quizzes', json={"previous_questions":[2,4,6,10],"quiz_category":{"id":"2","type":"art"}})
        data = json.loads(response.data)

        self.assertEqual(response.status_code,405) 
        self.assertEqual(data['success'],False)
        self.assertTrue(data['message'],'The method is not allowed for the requested URL.')   
         
        
      
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()