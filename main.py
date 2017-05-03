import csv
from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/', methods=['GET'])
def list_questions():
    """
    Displays list of questions.
    Loads data from question.csv file, sorted by time.
    Sorting of data will be here.
    """
    questions = data_manager.get_datatable_from_file('question.csv')
    return render_template('list.html', questions=questions)


@app.route('/question/new', methods=['GET'])
def new_question():
    """
    We arrive here from the list.html "ask question" button.
    Displays an empty question form.
    """
    return render_template('question_form.html')


@app.route('/question/<int:question_id>')
def question(question_id, methods=['GET']):
    """
    Displays the the requested question and the answers to it if they exist.
    We arrive here from '/',
    and from 'question/question_id/new_answer' (returning here after posting a new answer to the question)
    """

    return render_template('question_details.html')


@app.route('/question/<int:question_id>')
def save_new_question(question_id, methods=['POST']):
    """
    Displays the details of a question after saving it as a new question from 'question/new/'
    """
    return render_template('question_details.html', question=question)


@app.route('/question/<int:question_id>/new_answer', methods=['GET'])
def new_answer_form(question_id):
    """
    Displays empty form for entering an answer to the selected question (also displays question on top).
    We arrive here from '/question/question_id/'
    """
    return render_template('answer_form.html', form_action='/question/' + str(question_id) + '/new_answer')


@app.route('/question/<int:question_id>/new_answer', methods=['POST'])
def new_answer_post(question_id):
    """
    Handles the POST request coming from answer_form.html.
    """
    # TODO: Check validity of request.form['answer'] (min 10 char).
    # TODO: Append request.form['answer'] to answer.csv
    return render_template('question_details.html')


if __name__ == '__main__':
    app.run()
