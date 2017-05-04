import csv
from flask import Flask, render_template, request, url_for, redirect

import common
import data_manager

"""
Global variables for decoding specific columns in data
@DATA_TIME_INDEX: Unix timestamped column
@QUESTION_B64_COL: Base64 coded columns in question.csv
@ANSWER_B64_COL: Base64 coded columns in answer.csv
"""
DATA_TIME_INDEX = 1
QUESTION_B64_COL = (4, 5, 6)
ANSWER_B64_COL = (4, 5)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def list_questions():
    """
    Displays list of questions.
    Loads data from question.csv file, sorted by time.
    Sorting of data will be here.
    """
    questions = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
    questions[1:].sort(key=lambda question: question[DATA_TIME_INDEX])
    for i in range(1, len(questions)):
        questions[i][DATA_TIME_INDEX] = data_manager.decode_time(questions[i][DATA_TIME_INDEX])
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
    question = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)[question_id]
    all_answers = data_manager.get_datatable_from_file('data/answer.csv', ANSWER_B64_COL)
    answers_to_question_id = []
    for ans in all_answers:
        if str(question_id) == ans[3]:
            answers_to_question_id.append(ans)

    for answer in answers_to_question_id:
        answer[DATA_TIME_INDEX] = data_manager.decode_time(answer[DATA_TIME_INDEX])
    return render_template('question_details.html', question=question, answers=answers_to_question_id)


@app.route('/question/<int:question_id>/new_answer', methods=['GET'])
def new_answer_form(question_id):
    """
    Displays empty form for entering an answer to the selected question (also displays question on top).
    We arrive here from '/question/question_id/'
    """
    question = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)[question_id]
    return render_template('answer_form.html', question=question)


@app.route('/question/new_id', methods=['POST'])
def new_question_id():
    # TODO: time stamp generator
    # TODO: generate new ID
    # TODO: init numbers
    # TODO: sending data with format
    print(request.form)
    button_value = request.form["button"]
    if button_value == "Post Question":
        data = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
        new_question = common.get_new_question(data, request.form)
        return redirect("/question/" + str(new_question[0]))
    if button_value.isdigit():
        print(button_value)
        data = data_manager.get_datatable_from_file('data/answer.csv', ANSWER_B64_COL)
        new_answer = common.get_new_answer(data, request.form, button_value)
        return redirect("/question/" + button_value)


if __name__ == '__main__':
    app.run(debug=True)
