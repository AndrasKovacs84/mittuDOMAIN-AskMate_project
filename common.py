import data_manager


# ID;Submisson Time;View Number;Vote Number;Title;Message;Image
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
    print(new_question)
    data_manager.append_datatable_to_file("/data/question.csv", new_question, (4, 5, 6))
    return new_question


# ID;Submisson Time;Vote Number;Question ID;Message;Image
def get_new_answer(data, req_form, question_id):
    idx = str(int(data[-1][0]) + 1)
    local_time = data_manager.get_unixtime()
    view_number = "0"
    question_id = question_id
    message = req_form["answer"]
    image = ""
    new_answer = [idx, local_time, view_number, question_id,
                  message, image]
    data_manager.append_datatable_to_file("/data/answer.csv", new_answer, (4, 5))
    print(new_answer)
    return data
