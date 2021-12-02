#!/usr/bin/env python

# Puzzle 
# https://adventofcode.com/2020/day/6


def survey_customs_questions(filename):
    count = 0
    with open(filename) as f:
        data = f.read()
        record_list = data.split('\n\n')
        for record in record_list:
            record = record.replace('\n','')
            questions = set() 
            for q in record:
                questions.add(q)
            count+=len(questions)
    return count

def survey_customs_questions_correct(filename):
    count = 0
    with open(filename) as f:
        data = f.read()
        groups = data.split('\n\n')
        for group in groups:
            qa_tally = {}
            people = group.split('\n')
            for person in people:
                for question in person:
                    if question not in qa_tally:
                        qa_tally[question] = 1
                    else:
                        qa_tally[question] += 1
            for q_key, answer_count in qa_tally.items():
                if answer_count == len(people):
                    count += 1
    return count


if __name__ == "__main__":
    questions_answered = survey_customs_questions('day_6/customs_questions.txt')
    print('Part 1: ', questions_answered)
    questions_answered = survey_customs_questions_correct('day_6/customs_questions.txt')
    print('Part 2: ', questions_answered)