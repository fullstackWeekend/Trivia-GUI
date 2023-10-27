import PySimpleGUI as sg

# Define the list of questions and their corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Earth", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Mark Twain", "Charles Dickens", "Jane Austen", "William Shakespeare"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Giraffe", "Elephant", "Blue Whale", "Hippopotamus"],
        "answer": "Blue Whale"
    },
    # Add more questions here
]

# Create a PySimpleGUI window
layout = [
    [sg.Text("General Knowledge Quiz", font=("Helvetica", 20))],
    [sg.Text("", size=(40, 1))],
    [sg.Text("", size=(40, 1), key='-QUESTION-')],
    [sg.Radio("", "RADIO", key='-OPTION1-'), sg.Text("", size=(40, 1), key='-ANSWER1-')],
    [sg.Radio("", "RADIO", key='-OPTION2-'), sg.Text("", size=(40, 1), key='-ANSWER2-')],
    [sg.Radio("", "RADIO", key='-OPTION3-'), sg.Text("", size=(40, 1), key='-ANSWER3-')],
    [sg.Radio("", "RADIO", key='-OPTION4-'), sg.Text("", size=(40, 1), key='-ANSWER4-')],
    [sg.Button("Next"), sg.Button("Submit"), sg.Button("Exit")],
]

window = sg.Window("Quiz App", layout, finalize=True)

current_question = 0
score = 0

# Function to update the question and options
def update_question(question_num):
    question_data = questions[question_num]
    window['-QUESTION-'].update(question_data['question'])
    options = question_data['options']
    window['-OPTION1-'].update(text=options[0], value=1)
    window['-OPTION2-'].update(text=options[1], value=2)
    window['-OPTION3-'].update(text=options[2], value=3)
    window['-OPTION4-'].update(text=options[3], value=4)
    window['-ANSWER1-'].update("")
    window['-ANSWER2-'].update("")
    window['-ANSWER3-'].update("")
    window['-ANSWER4-'].update("")

# Initial question
update_question(current_question)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Next':
        # Reset Radio elements
        for i in range(4):
            window[f'-OPTION{i + 1}-'].update(value=False)

        user_answer = None
        for i in range(4):
            if values['-OPTION' + str(i + 1) + '-']:
                user_answer = questions[current_question]['options'][i]
                break

        correct_answer = questions[current_question]['answer']
        if user_answer == correct_answer:
            score += 1

        current_question += 1

        if current_question < len(questions):
            update_question(current_question)
            # Disable the "Next" button on the last question
            if current_question == len(questions) - 1:
                window['Next'].update(disabled=True)
        else:
            sg.popup(f"Quiz Complete!\nYour Score: {score}/{len(questions)}")
            break

    if event == 'Submit':
        # Reset Radio elements
        for i in range(4):
            window[f'-OPTION{i + 1}-'].update(value=False)

        user_answer = None
        for i in range(4):
            if values['-OPTION' + str(i + 1) + '-']:
                user_answer = questions[current_question]['options'][i]
                break

        correct_answer = questions[current_question]['answer']
        if user_answer == correct_answer:
            score += 1

        sg.popup(f"Quiz Complete!\nYour Score: {score}/{len(questions)}")
        break

window.close()