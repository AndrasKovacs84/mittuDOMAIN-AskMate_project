import csv
from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/', request, methods=['GET'])
def list_questions():
    """
    Displays list of questions.
    Loads data from question.csv file, sorted by time.
    Sorting of data will be here.
    """
    questions = data_manager.get_datatable_from_file('question.csv')
    return render_template('list.html', questions=questions)


@app.route('/question/new', methods=['GET', 'POST'])
def new_question():
    """
    We arrive here from the list.html "ask question" button.
    Displays an empty question form.
    """
    return render_template('question_form.html')


@app.route('/question/<int:question_id>')
def question(question_id):
    """
    Displays the the requested question and the answers to it if they exist.
    We arrive here from '/' (selected in list with "details" btn), 'question/new/' (after creating a new question),
    and from 'question/question_id/new_answer' (returning here after posting a new answer to the question)
    """
    return render_template('question_details.html')


@app.route('/question/<int:question_id>/new_answer')
def new_answer(question_id):
    """
    Displays empty form for entering an answer to the selected question (also displays question on top).
    We arrive here from '/question/question_id/'
    """
    return render_template('answer_form.html')


if __name__ == '__main__':
    app.run()