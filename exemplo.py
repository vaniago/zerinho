'''Gera questões de múltipla escolha dentro de um colab notebook
como em 
https://github.com/jupyter-widgets/ipywidgets/issues/2487
por
https://github.com/zxzhaixiang
Data: 27/02/2022
'''

import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output
#acréscimo para simplificar o esquema de cores
from termcolor import colored


def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativa = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativa.value)
        if a==correct_answer_index:
            s=colored("Correto!",'white','on_green')
        else:
            s=colored("Ops! Errou.",'white','on_red')
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="confirma")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativa, check, feedback_out])
    

#Insira aqui as questões
Q1 = create_multipleChoice_widget('blablabla',['apple','banana','pear'],'pear')
Q2 = create_multipleChoice_widget('lalalalal',['cat','dog','mouse'],'dog')
Q3 = create_multipleChoice_widget('jajajajaj',['blue','white','red'],'white')



#display(Q1)
#display(Q2)
#display(Q3)
