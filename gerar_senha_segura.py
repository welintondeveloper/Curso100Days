import random
import string
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox, simpledialog

# Função para gerar uma chave e salvar em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

# Função para carregar a chave do arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para criptografar uma mensagem
def criptografar_mensagem(mensagem, chave):
    f = Fernet(chave)
    mensagem_encriptada = f.encrypt(mensagem.encode())
    return mensagem_encriptada

# Função para descriptografar uma mensagem
def descriptografar_mensagem(mensagem_encriptada, chave):
    f = Fernet(chave)
    mensagem_decriptada = f.decrypt(mensagem_encriptada).decode()
    return mensagem_decriptada

def gerar_senha(num_esp, num_letras, num_nums):
    # Caracteres especiais
    caracteres_especiais = '!@#$%^&*()-_+=<>?'
    senha = []

    # Adicionar caracteres especiais
    senha += random.choices(caracteres_especiais, k=num_esp)

    # Adicionar letras (maiúsculas e minúsculas)
    letras = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    senha += random.choices(letras, k=num_letras)

    # Adicionar números
    numeros = string.digits  # 0123456789
    senha += random.choices(numeros, k=num_nums)

    # Embaralhar a senha para garantir aleatoriedade
    random.shuffle(senha)

    # Combinar todos os caracteres em uma string
    senha_final = ''.join(senha)

    return senha_final

def salvar_senha(nome_app, senha, chave):
    senha_encriptada = criptografar_mensagem(senha, chave)
    nome_app_encriptado = criptografar_mensagem(nome_app, chave)

    # Salvar o nome do aplicativo e a senha criptografada em um arquivo
    with open("senhas.txt", "ab") as file:
        file.write(nome_app_encriptado + b"\n")
        file.write(senha_encriptada + b"\n")

def ler_senhas(chave):
    try:
        with open("senhas.txt", "rb") as file:
            linhas = file.readlines()

        senhas = []
        for i in range(0, len(linhas), 2):
            nome_app = descriptografar_mensagem(linhas[i].strip(), chave)
            senha = descriptografar_mensagem(linhas[i+1].strip(), chave)
            senhas.append((nome_app, senha))

        # Criar uma nova janela para exibir as senhas
        janela_senhas = tk.Toplevel()
        janela_senhas.title("Senhas Salvas")

        for idx, (nome_app, senha) in enumerate(senhas):
            tk.Label(janela_senhas, text=f"Aplicativo: {nome_app}").grid(row=idx, column=0, padx=10, pady=5)
            tk.Entry(janela_senhas, width=30, state='readonly').grid(row=idx, column=1, padx=10, pady=5)
            tk.Button(janela_senhas, text="Copiar", command=lambda s=senha: copiar_para_area_transferencia(s)).grid(row=idx, column=2, padx=10, pady=5)

    except FileNotFoundError:
        messagebox.showinfo("Senhas Salvas", "Nenhuma senha salva ainda.")

def copiar_para_area_transferencia(senha):
    root.clipboard_clear()
    root.clipboard_append(senha)
    root.update()  # Atualiza a interface para refletir as mudanças
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

def configurar_senha_mestra():
    chave = carregar_chave()
    try:
        with open("senha_mestra.txt", "rb") as file:
            linhas = file.readlines()
            pergunta_secreta = descriptografar_mensagem(linhas[1].strip(), chave)
            resposta_secreta = descriptografar_mensagem(linhas[2].strip(), chave)

        resposta_inserida = simpledialog.askstring("Verificação", pergunta_secreta, show='*')
        if resposta_inserida != resposta_secreta:
            messagebox.showerror("Erro", "Resposta secreta incorreta.")
            return

    except FileNotFoundError:
        pass  # Primeira configuração, não há necessidade de verificar a resposta secreta

    senha_mestra = simpledialog.askstring("Senha Mestra", "Crie uma nova senha mestra:", show='*')
    pergunta_secreta = simpledialog.askstring("Pergunta Secreta", "Digite uma nova pergunta secreta para recuperar a senha mestra:")
    resposta_secreta = simpledialog.askstring("Resposta Secreta", "Digite a resposta para a nova pergunta secreta:")

    senha_mestra_encriptada = criptografar_mensagem(senha_mestra, chave)
    pergunta_secreta_encriptada = criptografar_mensagem(pergunta_secreta, chave)
    resposta_secreta_encriptada = criptografar_mensagem(resposta_secreta, chave)

    with open("senha_mestra.txt", "wb") as file:
        file.write(senha_mestra_encriptada + b"\n")
        file.write(pergunta_secreta_encriptada + b"\n")
        file.write(resposta_secreta_encriptada + b"\n")

def verificar_senha_mestra():
    chave = carregar_chave()
    try:
        with open("senha_mestra.txt", "rb") as file:
            linhas = file.readlines()
            senha_mestra = descriptografar_mensagem(linhas[0].strip(), chave)
    except FileNotFoundError:
        messagebox.showinfo("Configuração", "Configuração inicial: Por favor, crie uma senha mestra.")
        configurar_senha_mestra()
        return True

    senha_inserida = simpledialog.askstring("Senha Mestra", "Digite a senha mestra:", show='*')
    if senha_inserida == senha_mestra:
        return True
    else:
        resposta = messagebox.askquestion("Senha Incorreta", "Senha incorreta. Deseja redefinir a senha mestra?")
        if resposta == 'yes':
            recuperar_senha_mestra()
        return False

def recuperar_senha_mestra():
    chave = carregar_chave()
    try:
        with open("senha_mestra.txt", "rb") as file:
            linhas = file.readlines()
            pergunta_secreta = descriptografar_mensagem(linhas[1].strip(), chave)
            resposta_secreta = descriptografar_mensagem(linhas[2].strip(), chave)

        resposta_inserida = simpledialog.askstring("Recuperar Senha Mestra", pergunta_secreta, show='*')
        if resposta_inserida == resposta_secreta:
            configurar_senha_mestra()
        else:
            messagebox.showerror("Erro", "Resposta secreta incorreta.")
    except FileNotFoundError:
        messagebox.showinfo("Erro", "Nenhuma configuração de senha mestra encontrada.")

def gerar_senha_interface():
    try:
        num_esp = int(entry_esp.get())
        num_letras = int(entry_letras.get())
        num_nums = int(entry_nums.get())
        senha = gerar_senha(num_esp, num_letras, num_nums)
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def salvar_senha_interface():
    nome_app = entry_app.get()
    senha = entry_senha.get()
    if nome_app and senha:
        chave = carregar_chave()
        salvar_senha(nome_app, senha, chave)
        messagebox.showinfo("Sucesso", "Senha salva com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha o nome do aplicativo e gere uma senha.")

# Interface gráfica com tkinter
def main():
    global entry_esp, entry_letras, entry_nums, entry_senha, entry_app, root

    # Gera e salva a chave, se não existir
    try:
        carregar_chave()
    except FileNotFoundError:
        gerar_chave()

    root = tk.Tk()
    root.title("Gerador de Senhas Seguras")

    tk.Label(root, text="Caracteres Especiais:").grid(row=0, column=0, padx=10, pady=10)
    entry_esp = tk.Entry(root)
    entry_esp.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Letras:").grid(row=1, column=0, padx=10, pady=10)
    entry_letras = tk.Entry(root)
    entry_letras.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Números:").grid(row=2, column=0, padx=10, pady=10)
    entry_nums = tk.Entry(root)
    entry_nums.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(root, text="Gerar Senha", command=gerar_senha_interface).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(root, text="Senha Gerada:").grid(row=4, column=0, padx=10, pady=10)
    entry_senha = tk.Entry(root)
    entry_senha.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(root, text="Nome do Aplicativo:").grid(row=5, column=0, padx=10, pady=10)
    entry_app = tk.Entry(root)
    entry_app.grid(row=5, column=1, padx=10, pady=10)

    tk.Button(root, text="Salvar Senha", command=salvar_senha_interface).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    tk.Button(root, text="Ver Senhas Salvas", command=lambda: verificar_senha_mestra() and ler_senhas(carregar_chave())).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    tk.Button(root, text="Configurar/Reconfigurar Senha Mestra", command=configurar_senha_mestra).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()


