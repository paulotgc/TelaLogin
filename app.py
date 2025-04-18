import customtkinter as ctk

# configuração da aparencia
ctk.set_appearance_mode('dark')

# criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuario é paulo e a senha 123456
    if usuario == 'paulo' and senha == '123456':
        resultado_login.configure(text='Login Feito com Sucesso',text_color='green')
    else:
        resultado_login.configure(text='Login Incorreto', text_color='red')

# criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criação dos campos
# Label
label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady = 10)

# entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady = 10)

# Label
label_senha = ctk.CTkLabel(app,text='Senha',)
label_senha.pack(pady = 10)

# entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha',show = '*')
campo_senha.pack(pady = 10)

# Button
botao_login = ctk.CTkButton(app,text='Login', command=validar_login)
botao_login.pack(pady = 10)

# Campo feedback de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady = 10)


# inicia o loop da aplicação
app.mainloop()
