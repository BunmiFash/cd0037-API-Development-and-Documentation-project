import os
import re
import json
from unicodedata import category
from xml.dom.expatbuilder import parseFragmentString
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys

from models import *

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    db = SQLAlchemy(app)
       

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    cors = CORS(app, resources={
                r"/api/*": {"origins": "*"}})  

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response



    def paginate(request, questions):
        page = request.args.get('page', 1 , type = int)
        start = (page -1)* QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        question= [question.format() for question in questions]
        current_questions = question[start:end]
        return current_questions
 
    @app.route('/categories', methods = ['GET'])
    def get_all_categories():
        try:
            categories = Category.query.order_by(Category.id).all()
            category = {category.id:category.type for category in categories}
            return jsonify({
                "success": True,
                'categories':category,
                "num_of_categories":len(categories)
            })
        except:
            abort (404)

    @app.route('/questions', methods = ['GET'])
    def get_questions():
        try:
            questions = Question.query.all()
            current_questions = paginate(request, questions)
            categories = Category.query.order_by(Category.id).all()
            category = {category.id:category.type for category in categories}
      
            current_category = db.session.query(Category.type).join(Question, Category.id==Question.category).first()
            current_cat = {}
            for cat in current_category:
                current_cat = cat.format()
            if len(current_questions)<=0:
                abort(404)
                
        except:
            abort(404)

        finally:
            return jsonify({
                    'success':True,
                    'questions': current_questions,
                    'totalQuestions':len(questions),
                    'categories':category,
                    'currentCategory':current_cat
                })
              
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate(request, questions)

            return jsonify({
                'success': True,
                'deleted_question': question_id,
                'questions':current_questions,
                'totalQuestions':len(Question.query.all()),
            })

        except:
            abort(422)    


    @app.route('/questions/create', methods=['POST'])
    def post_new_question():        
        try:
            body = request.get_json()
            question = body.get('question', None)
            answer = body.get('answer', None)
            difficulty = body.get('difficulty', None)
            category = body.get('category',None)
            new_question = Question(question=question, answer=answer,category=category,difficulty=difficulty)
            new_question.insert()

        except:
            print(sys.exc_info())
            abort(405)

        finally:
            return jsonify({
                'success':True
                # 'question': pagedQuestion,
                # 'total_questions':len(Question.query.all())
            })

    @app.route('/questions/search',methods=['POST'])
    def search_question():
        searchTerm = request.json['searchTerm']
        searched_question = Question.query.filter(Question.question.ilike('%{}%'.format(searchTerm))).all()
        try:
           
            current_question = paginate(request, searched_question)
            category = db.session.query(Category.type).join(Question, Category.id==Question.category).first()
            current_cat = {}
            for cat in category:
                current_cat = cat.format()
        except:
            abort(404)
        finally:
            return jsonify({
                'success':True,
                'questions':current_question,
                'totalQuestions':len(searched_question),
                'currentCategory':current_cat
            })

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:question_category>/questions', methods=['GET'])
    def get_question(question_category):
        category = db.session.query(Category.type).join(Question, Category.id==question_category).first()
        current_cat = {}
        if category is not None:
            for cat in category:
                current_cat = cat.format()
            
        try:
            question = Question.query.filter(Question.category==question_category).all()
            current_questions = paginate(request, question)
        except:
           abort(400)
        finally:
            # print(category)
            return jsonify({
                'success':True,
                'questions':current_questions,
                'totalQuestions':len(current_questions),
                'currentCategory':current_cat
        
            })

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()
            quiz_category = body.get('quiz_category', None)
            prev_questions = body.get('previous_questions', None)
            selected_category = quiz_category.get('id')

        #     if selected_category != 0:
        #         questions = Question.query.filter(Question.id.notin_(prev_questions),Question.category==selected_category).all()
        #         # quiz = [question for question in questions if question not in prev_questions]

        #     else:
        #         questions = Question.query.filter(Question.id.not_in_(prev_questions)).all()
        #         # quiz = [question for question in questions if question not in prev_questions]

        #     if questions:
        #         quiz_question = random.choice(questions)
        #     else:
        #         quiz_question = None
            
        #     return jsonify({
        #         'success':True,
        #         'question':quiz_question.format()
        #     })
        # except:
        #     abort(422)

            
            if selected_category !=0:
                available_questions = Question.query.filter(Question.category==selected_category).all()
                question_list = [question.id for question in available_questions]
                quiz_questions = random.choice([question for question in question_list if question not in prev_questions])
                question = Question.query.filter(Question.category==selected_category, Question.id==quiz_questions).one_or_none()
             
                return jsonify({
                'success':True,
                'question':question.format()
            })    
                
            else:
                available_questions_for_all =Question.query.all()
                question_list_for_all = [question.id for question in available_questions_for_all]
                quiz_questions_for_all = random.choice([question for question in question_list_for_all if question not in prev_questions])
                question = Question.query.filter(Question.id==quiz_questions_for_all).one_or_none()
                # if quiz_questions_for_all is None:
                #    quiz_question_for_all = None
               
                return jsonify({
                'success':True,
                'question': question.format()
            })   

            
        except:
            abort(422)    
        


   
            

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message':'Resource Not Found',
            'error':404,
            'error_name':f'{error}'
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': f'Bad Request:{error.description}',
            'error_name':f'{error}'
        }), 400 

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'message':'The request was well-formed but was unable to be followed due to semantic errors.',
            'error': 422
        }), 422 

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message':'The method is not allowed for the requested URL.',
            'error': 405
        }), 405

    @app.errorhandler(500)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message':'Internal server error.',
            'error': 500
        }), 500

    return app

