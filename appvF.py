import PySimpleGUI as sg
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
nltk.download('words')
from nltk.corpus import words
layout = [
	[
		sg.Text('Enter the Incorrect Word', size =(20, 1)), sg.InputText(key = '-INPUT-'), 
		sg.Button('Correct', key = '-CORRECT-')
	],
	[sg.Text('Output', key = '-OUTPUT-')],
	[sg.Text('This app is made by Atharva,Aman,Afreen and Ashish', key = '-MADEBY-')]
]
correct_words = words.words()



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
				 for w in correct_words if w[0]==incorrect_words[0]]	  
			output = sorted(temp, key = lambda val:val[0])[0][1]
			output_string = 'Corrected Spelling is ' + output
			window['-OUTPUT-'].update(output_string)
			window['-MADEBY-']

window.close()