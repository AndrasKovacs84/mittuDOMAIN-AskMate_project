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


# Delete data by question ID, writeing to file
#
# @data_rout: string - csv file rout
# @question_id: int - marked question id to delete
# @decode_columns: tuple of int - decodeable columns
# @id_column: int - which column hase the question ID
def delete_data_by_id(data_rout, question_id, decode_columns, id_column):
    data = data_manager.get_datatable_from_file(data_rout, decode_columns)
    new_data = [row for row in data if row[id_column] != str(question_id)]
    data_manager.write_datatable_to_file(data_rout, new_data, decode_columns)
    return new_data


# selecting question by ID returning that question details
#
# @path_as_string: string - csv file rout
# @question_id: int - marked question id to delete
# @decode_columns: tuple of int - decodeable columns
# @id: int - the ID you are looking for
def lookup_item_by_id(path_as_string, decode_columns, id):
    data = data_manager.get_datatable_from_file(path_as_string, decode_columns)
    for entry in data:
        if entry[0] == str(id):
            return entry


# selecting question by ID
#
# @question_id: int - marked question id to delete
# @question: tuple of int - decodeable columns
def search_row_by_id(question_id, question):
    for row in question[1:]:
        if int(row[0]) == question_id:
            return row
