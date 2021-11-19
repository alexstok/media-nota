'''
Programa que ler o nome do aluno, idade, série e determina as notas de acordo com o usuário (PySimpleGUI)
'''

# importe da(s) biblioteca(s) necessária(s)
import PySimpleGUI as sg

sg.theme('DarkGrey13') # Tema opcional
# Criação do layout
layout = [
    [sg.Text('Nome'), sg.Input(size=(30,1), key='nome')],
    [sg.Text('Idade '), sg.Input(size=(5,1), justification='center', key='idade'), sg.Text('Série'), sg.Input(size=(5,1), justification='center', key='serie')],
    [sg.Text('-'*65)],
    [sg.Text('Nota 1'), sg.Input(size=(5,1), justification='center', key='nota1'), sg.Text('Nota 2'), sg.Input(size=(5,1), justification='center', key='nota3')],
    [sg.Text('Nota 3'), sg.Input(size=(5,1), justification='center', key='nota2'), sg.Text('Nota 4'), sg.Input(size=(5,1), justification='center', key='nota4')],
    [sg.Text('Média:'), sg.Text(size=(4,1), key='media')],
    [sg.Text('PREENCHA TODOS OS CAMPOS!', key='aviso', visible=False, text_color='red')],
    [sg.Button('Calcular', button_color=('black', 'white'), size=(15,1)), sg.Button('Limpar', button_color=('black', 'white'), size=(15,1))],
    [sg.Output(size=(35,7), key='output')],
]

window = sg.Window('Notas-Aluno', layout=layout, finalize=True)

# Loop de eventos para o programa não ser finalizado
while True:
    events, values = window.Read()
    if events == sg.WIN_CLOSED:
        break
    # Se os eventos não forem escritos corretamente
    if events == 'Calcular' and values['nome'] == '' or values['idade'] == '' or values['nota1'] == '' or values['nota2'] == '' or values['nota3'] == '' or values['nota4'] == '':
        window.Element('aviso').Update(visible=True)
    # Se os eventos forem escritos corretamente
    if events == 'Calcular' and values['nome'] != '' and values['idade'] != '' and values['nota1'] != '' and values['nota2'] != '' and values['nota3'] != '' and values['nota4'] != '':
        window.Element('aviso').Update(visible=False)
        nota1 = float(values['nota1'].replace(',', '.'))
        nota2 = float(values['nota2'].replace(',', '.'))
        nota3 = float(values['nota3'].replace(',', '.'))
        nota4 = float(values['nota4'].replace(',', '.'))
        media = (nota1 + nota2 + nota3 + nota4) / 4
        media = round(media, 1)
        window.Element('media').Update(value=media)
        nome = values['nome']
        if (media < 4.5):
            print('RESULTADO\n')
            print(f'Aluno(a): {nome}\nMédia: ', media)
            print('Aluno(a) Reprovado(a)')
        elif (media >= 4.5 and media <= 6.9):
            print('RESULTADO\n')
            print(f'Aluno(a): {nome}\nMédia: ', media)
            print('Aluno(a) em Recuperação(a)')
        else:
            print('RESULTADO\n')
            print(f'Aluno(a): {nome}\nMédia: ', media)
            print('Aluno(a) Aprovado(a)')
    # Evento do comando limpar
    if events == 'Limpar':
        window.Element('nome').Update(value='')
        window.Element('idade').Update(value='')
        window.Element('serie').Update(value='')
        window.Element('nota1').Update(value='')
        window.Element('nota2').Update(value='')
        window.Element('nota3').Update(value='')
        window.Element('nota4').Update(value='')
        window.Element('media').Update(value='')
        window.Element('output').Update(value='')
