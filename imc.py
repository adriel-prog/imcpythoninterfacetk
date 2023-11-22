import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # Lógica para o cálculo do IMC
        imc = peso / (altura ** 2)

        # Exibir o resultado do IMC
        resultado_imc.set(f"IMC: {imc:.2f}")

        # Análise do resultado
        if imc < 18.5:
            messagebox.showinfo("Análise", "Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            messagebox.showinfo("Análise", "Peso normal")
        elif 25 <= imc < 29.9:
            messagebox.showinfo("Análise", "Sobrepeso")
        elif 30 <= imc < 34.9:
            messagebox.showinfo("Análise", "Obesidade leve")
        elif 35 <= imc < 39.9:
            messagebox.showinfo("Análise", "Obesidade moderada")
        else:
            messagebox.showinfo("Análise", "Obesidade grave")

    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira valores numéricos válidos.")


def limpar_campos():
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    resultado_imc.set("IMC: ")


# Criar a janela principal
root = tk.Tk()
root.title("Calculadora IMC")

# Variáveis para armazenar os valores
resultado_imc = tk.StringVar()

# Configuração de fontes e cores
font_label = ("Helvetica", 14)
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")

# Configurar a janela
root.configure(bg="#d2f5d2")  # Verde claro

# Rótulos e caixas de entrada
label_peso = tk.Label(root, text="Peso:", font=font_label,
                      bg="#d2f5d2", fg="#333333")  # Verde claro e texto escuro
label_peso.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_peso = tk.Entry(root, font=font_entry)
entry_peso.grid(row=0, column=1, padx=10, pady=10, sticky="w")

label_altura = tk.Label(root, text="Altura:", font=font_label,
                        bg="#d2f5d2", fg="#333333")  # Verde claro e texto escuro
label_altura.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_altura = tk.Entry(root, font=font_entry)
entry_altura.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Botão de cálculo
btn_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc,
                         font=font_button, bg="#4CAF50", fg="#ffffff")  # Verde escuro e texto branco
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="we")

# Botão para limpar os campos
btn_limpar = tk.Button(root, text="Limpar Campos", command=limpar_campos,
                       font=font_button, bg="#4CAF50", fg="#ffffff")  # Verde escuro e texto branco
btn_limpar.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="we")

# Etiqueta para exibir o resultado
lbl_resultado = tk.Label(root, textvariable=resultado_imc, font=font_label,
                         bg="#d2f5d2", fg="#333333")  # Verde claro e texto escuro
lbl_resultado.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="w")

# Centralizar a janela
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))

# Iniciar o loop da interface gráfica
root.mainloop()
