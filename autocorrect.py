import PySimpleGUI as sg
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
nltk.download('words')
import re
from nltk.corpus import words
layout = [
	[
		sg.Text('Enter the Incorrect Word', size =(20, 1)), sg.InputText(key = '-INPUT-'), 
		sg.Button('Correct', key = '-CORRECT-')
	],
	[sg.Text('Output', key = '-OUTPUT-')],
	[sg.Text('This app is made by Atharva,Aman,Afreen and Ashish under guidance of Dr Jayavrinda', key = '-MADEBY-')]
]
correct_words = words.words()

def process_text(path):
    words1 = []
    with open(path) as f:
        file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words1 = re.findall(r'\w+',file_name_data)

    return words1

book_words = process_text('kidsbook.txt')


window = sg.Window('AutoCorrect Using NLP',layout)

while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-CORRECT-':
		incorrect_words = values['-INPUT-']
		if incorrect_words.isnumeric():
			window['-OUTPUT-'].update('Please enter a word')
		else:
			temp = [(jaccard_distance(set(ngrams(incorrect_words, 2)),
                            set(ngrams(w, 2))),w)
							#to change dictionary edit the next line book_words, correct_words
				for w in book_words if w[0]==incorrect_words[0]]	 
			output = sorted(temp, key = lambda val:val[0])[0][1]
			output_string = 'Corrected Spelling is ' + output
			window['-OUTPUT-'].update(output_string)
			window['-MADEBY-']

window.close()