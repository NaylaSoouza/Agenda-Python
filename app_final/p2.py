# Projeto: Calendário e Lista de Tarefas
# Descrição: Um aplicativo que permite ao usuário visualizar um calendário de um ano específico e adicionar tarefas com datas, organizando suas atividades.
# Funcionalidades:
# 1. Gerar um calendário para um ano específico.
# 2. Adicionar tarefas com data e descrição.
# 3. Marcar tarefas como concluídas.  
# 4. Excluir tarefas da lista.
# Bibliotecas utilizadas: customtkinter, tkinter, calendar
#nomes : Nayla Francisco de Souza, Shaden Elsi, Beatriz Palaro

# Data de criação: 2024-06-15
# Observações: O aplicativo é projetado para ser simples e intuitivo, com uma interface amigável. Ele pode ser expandido no futuro para incluir funcionalidades adicionais, como lembretes ou integração com calendários online.
# Importação das bibliotecas necessárias
# A biblioteca customtkinter é usada para criar uma interface gráfica moderna e personalizável, enquanto a biblioteca calendar é utilizada para gerar o calendário do ano especificado pelo usuário. A biblioteca tkinter é usada para exibir mensagens de erro e criar a janela principal do aplicativo.
# A estrutura do código é organizada em funções para facilitar a manutenção e a leitura. A função show_calendar() é responsável por gerar e exibir o calendário, enquanto a função adicionar_tarefa() lida com a adição de tarefas à lista. O aplicativo é iniciado criando uma janela principal e configurando os elementos da interface, como botões, campos de entrada e labels.
# O aplicativo é projetado para ser responsivo e fácil de usar, permitindo que os usuários organizem suas tarefas e visualizem o calendário de forma eficiente. A interface é personalizada com cores e fontes para melhorar a experiência do usuário.
# O código inclui validação de entrada para garantir que o usuário insira um ano válido ao gerar o calendário e que os campos de data e tarefa sejam preenchidos ao adicionar uma nova tarefa. As tarefas podem ser marcadas como concluídas, alterando a cor do texto, e também podem ser excluídas da lista.
# O aplicativo é uma ferramenta útil para ajudar os usuários a manterem suas atividades organizadas e visualizarem seus compromissos de forma clara e acessível.
# O código a seguir é a implementação completa do aplicativo de calendário e lista de tarefas, utilizando as bibliotecas mencionadas para criar uma interface gráfica funcional e agradável. O aplicativo permite que os usuários gerem um calendário para um ano específico, adicionem tarefas com datas e descrições, marquem tarefas como concluídas e excluam tarefas da lista. A interface é projetada para ser intuitiva e fácil de usar, com validação de entrada para garantir que os dados inseridos sejam válidos. O aplicativo é uma ferramenta útil para ajudar os usuários a organizarem suas atividades e visualizarem seus compromissos de forma eficiente.

#Como usar esse código:
# 1. Certifique-se de ter a biblioteca customtkinter instalada. Você pode instalá-la usando pip:
#    pip install customtkinter  
# 2. Copie o código completo para um arquivo Python (.py) e execute-o. Isso abrirá a janela do aplicativo.
# 3. Para gerar um calendário, insira um ano válido no campo "Informe o Ano:" e clique no botão "Gerar Calendário". Uma nova janela aparecerá com o calendário do ano especificado.
# 4. Para adicionar uma tarefa, preencha os campos "Data para finalizar:" e "Tarefa:" com as informações correspondentes e clique no botão "Adicionar". A tarefa será adicionada à lista de tarefas cadastradas.
# 5. Para marcar uma tarefa como concluída, clique na caixa de seleção ao lado da tarefa. O texto da tarefa mudará de vermelho para verde para indicar que foi concluída.
# 6. Para excluir uma tarefa, clique no botão "excluir" ao lado da tarefa que deseja remover. A tarefa será removida da lista.  
# 7. Para sair do aplicativo, clique no botão "Sair" na parte inferior da janela principal. Isso fechará o aplicativo.
# Observação: Certifique-se de inserir um ano válido ao gerar o calendário e de preencher ambos os campos (data e tarefa) ao adicionar uma nova tarefa para evitar mensagens de erro. O formato da data deve ser "dd/mm/aaaa".
           

# =========================================================
# IMPORTAÇÕES   
# =========================================================

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import calendar

# =========================================================
# CONFIGURAÇÕES INICIAIS
# =========================================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Lista de tarefas
lista_de_tarefas = []


# =========================================================
# FUNÇÃO: MOSTRAR CALENDÁRIO
# =========================================================


def mostrar_calendario():

    # Verifica se o usuário digitou um ano válido
    try:
        ano = int(entrada_ano.get())

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um ano válido!"
        )
        return

    # -----------------------------------------------------
    # JANELA DO CALENDÁRIO
    # -----------------------------------------------------

    janela_calendario = ctk.CTkToplevel(app)
    janela_calendario.title(f"Calendário {ano}")
    janela_calendario.geometry("620x500")
    janela_calendario.configure(fg_color="#EAF3FF")

    # Mantém a janela na frente
    janela_calendario.lift()
    janela_calendario.attributes("-topmost", True)
    janela_calendario.after(
        10,
        lambda: janela_calendario.attributes("-topmost", False)
    )

    # -----------------------------------------------------
    # CARD DO CALENDÁRIO
    # -----------------------------------------------------

    frame_calendario = ctk.CTkFrame(
        janela_calendario,
        fg_color="white",
        corner_radius=20
    )

    frame_calendario.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # Título
    titulo_calendario = ctk.CTkLabel(
        frame_calendario,
        text=f"CALENDÁRIO {ano}",
        font=("Arial", 22, "bold"),
        text_color="#1565C0"
    )

    titulo_calendario.pack(pady=(20, 10))

    # Gera o calendário do ano
    calendario_ano = calendar.calendar(ano)

    # Mostra o calendário
    texto_calendario = ctk.CTkLabel(
        frame_calendario,
        text=calendario_ano,
        font=("Consolas", 11),
        justify="left",
        text_color="#1E3A5F"
    )

    texto_calendario.pack(padx=20, pady=10)


# =========================================================
# FUNÇÃO: ADICIONAR TAREFA
# =========================================================


def adicionar_tarefa():

    # Pega os dados digitados
    data = entrada_data.get()
    tarefa = entrada_tarefa.get()

    # -----------------------------------------------------
    # VALIDAÇÃO
    # -----------------------------------------------------

    if data == "" or tarefa == "":

        messagebox.showwarning(
            "Erro",
            "Preencha todos os campos!"
        )

        return

    # Junta data + tarefa
    item_tarefa = f"{data} - {tarefa}"

    # -----------------------------------------------------
    # CARD DA TAREFA
    # -----------------------------------------------------

    frame_tarefa = ctk.CTkFrame(
        lista_tarefas,
        fg_color="#F7F7FB",
        corner_radius=15,
        height=45
    )

    frame_tarefa.pack(
        fill="x",
        padx=5,
        pady=5
    )

    # -----------------------------------------------------
    # CHECKBOX
    # -----------------------------------------------------

    tarefa_concluida = tk.BooleanVar()

    checkbox_tarefa = ctk.CTkCheckBox(
        frame_tarefa,
        text=item_tarefa,
        variable=tarefa_concluida,
        font=("Arial", 14, "bold"),
        text_color="red",
        checkbox_width=18,
        checkbox_height=18
    )

    checkbox_tarefa.pack(
        side="left",
        padx=12,
        pady=8
    )

    # -----------------------------------------------------
    # MUDA COR DA TAREFA
    # -----------------------------------------------------

    def alterar_cor_tarefa():

        if tarefa_concluida.get():
            checkbox_tarefa.configure(text_color="green")

        else:
            checkbox_tarefa.configure(text_color="red")

    checkbox_tarefa.configure(command=alterar_cor_tarefa)

    # -----------------------------------------------------
    # BOTÃO EXCLUIR
    # -----------------------------------------------------

    botao_excluir = ctk.CTkButton(
        frame_tarefa,
        text="Excluir",
        width=35,
        height=30,
        fg_color="#FFE5E5",
        hover_color="#FFD1D1",
        text_color="red",
        corner_radius=50,
        command=frame_tarefa.destroy
    )

    botao_excluir.pack(
        side="right",
        padx=10
    )

    # -----------------------------------------------------
    # LIMPA OS CAMPOS
    # -----------------------------------------------------

    entrada_data.delete(0, "end")
    entrada_tarefa.delete(0, "end")


# =========================================================
# JANELA PRINCIPAL
# =========================================================

app = ctk.CTk()

app.title("CALENDÁRIO")
app.geometry("850x650")
app.configure(fg_color="#EAF3FF")


# =========================================================
# FRAME PRINCIPAL COM ROLAGEM
# =========================================================

main_frame = ctk.CTkScrollableFrame(
    app,
    fg_color="#EAF3FF"
)

main_frame.pack(
    fill="both",
    expand=True
)


# =========================================================
# TÍTULO PRINCIPAL
# =========================================================

label_titulo = ctk.CTkLabel(
    main_frame,
    text="Verifique o Calendário",
    font=("Arial", 28, "bold"),
    text_color="#0B1D4D"
)

label_titulo.pack(pady=(25, 5))


# =========================================================
# SUBTÍTULO
# =========================================================

label_subtitulo = ctk.CTkLabel(
    main_frame,
    text="Organize suas tarefas e mantenha seu ano em dia!",
    font=("Arial", 14),
    text_color="#5D6B8A"
)

label_subtitulo.pack(pady=(0, 20))


# =========================================================
# CARD DO ANO
# =========================================================

card_ano = ctk.CTkFrame(
    main_frame,
    fg_color="white",
    corner_radius=20,
    width=380
)

card_ano.pack(
    padx=20,
    pady=10
)

# Texto do ano
label_ano = ctk.CTkLabel(
    card_ano,
    text="Informe o Ano:",
    font=("Arial", 18, "bold"),
    text_color="#1B2A4E"
)

label_ano.pack(pady=(25, 10))

# Campo do ano
entrada_ano = ctk.CTkEntry(
    card_ano,
    width=250,
    height=38,
    corner_radius=12,
    font=("Arial", 18, "bold"),
    border_color="#2F80ED"
)

entrada_ano.pack()

# Botão do calendário
botao_calendario = ctk.CTkButton(
    card_ano,
    text="Gerar Calendário",
    width=180,
    height=38,
    corner_radius=12,
    font=("Arial", 16, "bold"),
    fg_color="#1E88FF",
    hover_color="#1565C0",
    command=mostrar_calendario
)

botao_calendario.pack(pady=20)


# =========================================================
# TÍTULO DAS ANOTAÇÕES
# =========================================================

label_anotacoes = ctk.CTkLabel(
    main_frame,
    text="Anotações",
    font=("Segoe UI", 24, "bold"),
    text_color="#1565C0"
)

label_anotacoes.pack(pady=20)


# =========================================================
# CARD DE TAREFAS
# =========================================================

card_tarefas = ctk.CTkFrame(
    main_frame,
    fg_color="white",
    corner_radius=20
)

card_tarefas.pack(
    fill="x",
    padx=40,
    pady=10
)

# Texto da data
label_data = ctk.CTkLabel(
    card_tarefas,
    text="Data para finalizar:",
    font=("Arial", 16, "bold"),
    text_color="#1B2A4E"
)

label_data.pack(
    anchor="w",
    padx=25,
    pady=(20, 5)
)

# Campo da data
entrada_data = ctk.CTkEntry(
    card_tarefas,
    height=35,
    corner_radius=10,
    placeholder_text="dd/mm/aaaa",
    font=("Arial", 14)
)

entrada_data.pack(
    fill="x",
    padx=25,
    pady=(0, 15)
)

# Texto da tarefa
label_tarefa = ctk.CTkLabel(
    card_tarefas,
    text="Tarefa:",
    font=("Arial", 16, "bold"),
    text_color="#1B2A4E"
)

label_tarefa.pack(
    anchor="w",
    padx=25,
    pady=(0, 5)
)

# Campo da tarefa
entrada_tarefa = ctk.CTkEntry(
    card_tarefas,
    height=35,
    corner_radius=10,
    placeholder_text="Descreva a tarefa...",
    font=("Arial", 14)
)

entrada_tarefa.pack(
    fill="x",
    padx=25,
    pady=(0, 15)
)

# Botão adicionar
botao_adicionar = ctk.CTkButton(
    card_tarefas,
    text="Adicionar",
    width=140,
    height=38,
    corner_radius=12,
    font=("Arial", 15, "bold"),
    fg_color="#18B85B",
    hover_color="#149447",
    command=adicionar_tarefa
)

botao_adicionar.pack(pady=15)


# =========================================================
# LISTA DE TAREFAS
# =========================================================

card_lista = ctk.CTkFrame(
    main_frame,
    fg_color="white",
    corner_radius=20
)

card_lista.pack(
    fill="x",
    padx=40,
    pady=15
)

# Título da lista
label_lista = ctk.CTkLabel(
    card_lista,
    text="Tarefas cadastradas",
    font=("Arial", 18, "bold"),
    text_color="#1E88FF"
)

label_lista.pack(
    anchor="w",
    padx=20,
    pady=15
)

# Área onde as tarefas aparecem
lista_tarefas = ctk.CTkFrame(
    card_lista,
    fg_color="transparent"
)

lista_tarefas.pack(
    fill="x",
    padx=15,
    pady=(0, 15)
)


# =========================================================
# BOTÃO SAIR
# =========================================================

botao_sair = ctk.CTkButton(
    main_frame,
    text="Sair",
    width=130,
    height=40,
    corner_radius=12,
    fg_color="#FF4D4D",
    hover_color="#D93636",
    font=("Arial", 16, "bold"),
    command=app.destroy
)

botao_sair.pack(pady=25)


# =========================================================
# EXECUTA O PROGRAMA
# =========================================================

app.mainloop()

