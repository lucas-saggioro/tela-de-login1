from PySimpleGUI import PySimpleGUI as sg
import tkinter as tk

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(30,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*', size=(30,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de Login', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'lucas' and valores ['senha'] == '123456':
            tk.messagebox.showinfo(title='Sucesso!', message='Login realizado com sucesso.')
    if eventos == 'Entrar':
        if valores['usuario'] != 'lucas' or valores ['senha'] != '123456':
            tk.messagebox.showinfo(title='Erro!', message='Usuário ou senha inválidos.')