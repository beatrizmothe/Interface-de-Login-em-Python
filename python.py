import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def validar():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == "" or senha == "":
        mensagem.configure(text=f"Os campos devem ser preenchidos!", text_color="red")
    else:
        mensagem.configure(text=f"Usuário Cadastrado!\nUsuário: {usuario}", text_color="green")


app = ctk.CTk()
app.title('Login')
app.geometry('400x400')

label = ctk.CTkLabel(app, text='Login')
label.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

ctk.CTkButton(app, text='Entrar', command=validar).pack(pady=20)

mensagem = ctk.CTkLabel(app, text="", font=('Arial', 12))
mensagem.pack(pady=10)

app.mainloop()
