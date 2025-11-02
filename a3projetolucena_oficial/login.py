import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("blue")
def validar_login(event=None):  # 🔹
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'wedson' and senha == '123456':
        resultado_login.configure(text='✅ Login feito com sucesso!', text_color='green')
    if usuario == 'admin' and senha == 'admin':
        resultado_login.configure(text='✅ Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='❌ Login incorreto', text_color='red')

# ------------------ APP ------------------
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('720x460')
app.minsize(500, 350)
app.state("zoomed")

# Configurar grid do app
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# ------------------ FRAME PRINCIPAL ------------------
frame_login = ctk.CTkFrame(app, corner_radius=15)
frame_login.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

# Centralizar conteúdo
frame_login.grid_rowconfigure((0,1,2,3,4), weight=1)
frame_login.grid_columnconfigure((0,1), weight=1)


titulo = ctk.CTkLabel(frame_login, text="🔐 Sistema de Login", font=("Arial", 24, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=20)


label_usuario = ctk.CTkLabel(frame_login, text='Email:')
label_usuario.grid(row=1, column=0, sticky="e", padx=10, pady=10)

campo_usuario = ctk.CTkEntry(frame_login, placeholder_text='Digite seu Email', width=300)
campo_usuario.grid(row=1, column=1, sticky="w", padx=10, pady=10)


label_senha = ctk.CTkLabel(frame_login, text='Senha:')
label_senha.grid(row=2, column=0, sticky="e", padx=10, pady=10)

campo_senha = ctk.CTkEntry(frame_login, placeholder_text='Digite sua Senha', show="*", width=300)
campo_senha.grid(row=2, column=1, sticky="w", padx=10, pady=10)


botao_login = ctk.CTkButton(frame_login, text='Entrar', command=validar_login, width=200, height=40, corner_radius=10)
botao_login.grid(row=3, column=0, columnspan=2, pady=20)

 
resultado_login = ctk.CTkLabel(frame_login, text='', font=("Arial", 14))
resultado_login.grid(row=4, column=0, columnspan=2, pady=10)

# ------------------ ENTER FUNCIONA COMO LOGIN ------------------
app.bind("<Return>", validar_login)  # 🔹 Enter em qualquer lugar
campo_senha.bind("<Return>", validar_login)  # 🔹 Enter específico no campo senha

app.mainloop()


