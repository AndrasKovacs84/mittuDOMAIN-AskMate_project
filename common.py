import data_manager


# Create new question with its elements in the csv
# CSV title: ID;Submisson Time;View Number;Vote Number;Title;Message;Image
#
# @data: list of list - whole answer table 
# @req_form: dictionary from html form 
def get_new_question(data, req_form):
    idx = str(int(data[-1][0]) + 1)
    local_time = data_manager.get_unixtime()
    view_number = "0"
    vote_number = "0"
    title = req_form["title"]
    data_form_story = req_form["story"]
    image = ""
    new_question = [idx, local_time, view_number, vote_number,
                    title, data_form_story, image]
    data_manager.append_datatable_to_file("/data/question.csv", new_question, (4, 5, 6))
    return new_question


# Create new answer with its elements in the csv
# CSV title: ID;Submisson Time;Vote Number;Question ID;Message;Image
#
# @data: list of list - whole answer table
# @req_form: dictionary from html form
# @question_id: int - index of the question
def get_new_answer(data, req_form, question_id):
    idx = str(int(data[-1][0]) + 1)
    local_time = data_manager.get_unixtime()
    view_number = "0"
    message = req_form["answer"]
    image = ""
    new_answer = [idx, local_time, view_number, question_id,
                  message, image]
    data_manager.append_datatable_to_file("/data/answer.csv", new_answer, (4, 5))
    return data


def delete_data_by_id(data, button_value, code_columns, question_id):
    new_data = [row for row in data if row[question_id] != button_value]
    data_manager.write_datatable_to_file("data/story.csv", new_data, code_columns)
    return new_data