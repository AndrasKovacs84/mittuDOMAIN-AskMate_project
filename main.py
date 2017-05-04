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
    Displays the list of questions.
    Loads data from question.csv file, sorted by time.
    """
    questions = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
    question_header = questions[0]
    questions = sorted(questions[1:], key=lambda question: int(question[DATA_TIME_INDEX]), reverse=True)
    for i in range(0, len(questions)):
        questions[i][DATA_TIME_INDEX] = data_manager.decode_time(questions[i][DATA_TIME_INDEX])
    questions.insert(0, question_header)
    return render_template('list.html', questions=questions)


@app.route('/question/new', methods=['GET'])
def new_question():
    """
    We arrive here from the list.html "ask question" button.
    Displays an empty question form.
    """
    question = []
    form_action = '/question/new_id'
    button_caption = 'Post Question'
    return render_template('question_form.html', form_action=form_action,
                           question=question, button_caption=button_caption)


@app.route('/question/<int:question_id>')
def question(question_id, methods=['GET']):
    """
    Displays the the requested question and the answers to it if they exist.
    We arrive here from '/',
    and from 'question/question_id/new_answer' (returning here after posting a new answer to the question)
    """
    question = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
    question = common.search_row_by_id(question_id, question)
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
    question = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
    question = common.search_row_by_id(question_id, question)
    return render_template('answer_form.html', question=question)


@app.route('/question/new_id', methods=['POST'])
def new_question_id():
    button_value = request.form["button"]
    if button_value == "Post Question":
        data = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
        new_question = common.get_new_question(data, request.form)
        return redirect("/question/" + str(new_question[0]))
    if button_value.isdigit():
        data = data_manager.get_datatable_from_file('data/answer.csv', ANSWER_B64_COL)
        new_answer = common.get_new_answer(data, request.form, button_value)
        return redirect("/question/" + button_value)


@app.route('/question/<int:question_id>/delete', methods=['GET'])
def delete_question(question_id):
    common.delete_data_by_id('data/question.csv', question_id, QUESTION_B64_COL, 0)
    common.delete_data_by_id('data/answer.csv', question_id, ANSWER_B64_COL, 3)
    return redirect("/")


@app.route('/question/<int:question_id>/edit', methods=['GET'])
def edit_question_form(question_id):
    question = common.lookup_item_by_id('data/question.csv', QUESTION_B64_COL, question_id)
    form_action = '/question/' + str(question_id)
    button_caption = 'Update Question'
    return render_template("question_form.html", question=question, form_action=form_action, button_caption=button_caption)


@app.route('/question/<int:question_id>', methods=['POST'])
def update_question(question_id):
    questions = data_manager.get_datatable_from_file('data/question.csv', QUESTION_B64_COL)
    print(request.form)
    for question in questions:
        if question[0] == str(question_id):
            question[4] = request.form["title"]
            question[5] = request.form['story']
            break
    data_manager.write_datatable_to_file('data/question.csv', questions, QUESTION_B64_COL)
    return redirect('/question/' + str(question_id))


if __name__ == '__main__':
    app.run(debug=True)
