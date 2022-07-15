# ***************************************************************************************
# 
# CODE BY Pham Van Minh K22 FIRA
# 
# ***************************************************************************************

from underthesea import word_tokenize
import numpy as np
import json
from CHATBOT_NLP_FINAL_CORE_V4.question_classification import question_classification
from CHATBOT_NLP_FINAL_CORE_V4.re_processing import question_re_processing_to_token

with open('CHATBOT_NLP_FINAL_CORE_V4/data/question.json', 'r', encoding='utf-8-sig') as f:
    questions = json.load(f)

def unique(list):
    result = []
    for x in list:
        if x not in result:
            result.append(x)
    return result

def get_question_pattern_token(type):
    token = []
    for i in questions['questions']:
        for x in i['patterns']:
            if i['type'] == type:
                token.append(word_tokenize(x))

    _token = []

    for i in token:
        for x in i:
            _token.append(x)
    result = unique(_token)

    return result

def question_analysis(question):
    question_type = question_classification(question)
    pattern_token = get_question_pattern_token(question_type)
    question_token = question_re_processing_to_token(question)
    question_p = []
    for x in question_token:
        core = []
        if x in pattern_token:
            core.append(x)
            core.append('<?>')
        else:
            core.append(x)
            core.append('<core>')
        question_p.append(core)

    result = {
                "type": question_type,
                "structure": question_p,
                                            }
    return result

if __name__ == "__main__":
    test = "đầu tư cổ phiếu tại đâu?"
    print(question_analysis(test))