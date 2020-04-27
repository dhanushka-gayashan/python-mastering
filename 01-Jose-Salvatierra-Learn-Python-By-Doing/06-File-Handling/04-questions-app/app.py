questions_file = open('questions.txt', 'r')
questions_list = [line.strip() for line in questions_file.readlines()]
questions_file.close()

score = 0
total = len(questions_list)

for line in questions_list:
    question, answer = line.split('=')
    user_answer = input('{}='.format(question))
    if answer == user_answer:
        score += 1

result_file = open('result.txt', 'w')
result_file.write('Your final score is {}/{}.'.format(score, total))
result_file.close()
