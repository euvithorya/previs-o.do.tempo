import tkinter as tk
from tkinter import messagebox
import requests

def obter_previsao():
    cidade = cidade_entry.get().strip()
    if not cidade:
        messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade.")
        return

    chave_api = "40f7be2cef1cbfbaa3296259f0b90766"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        dados = resposta.json()

        if dados["cod"] != 200:
            messagebox.showerror("Erro", f"Erro na API: {dados.get('message', 'Erro desconhecido')}")
            return

        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        humidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]

        resultado_label.config(
            text=(
                f"Temperatura: {temp}°C\n"
                f"Descrição: {descricao.capitalize()}\n"
                f"Humidade: {humidade}%\n"
                f"Vento: {vento} m/s"
            )
        )
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao conectar-se à API: {e}")

root = tk.Tk()
root.title("Previsão do Tempo")
root.geometry("300x250")

cidade_label = tk.Label(root, text="Digite o nome da cidade:")
cidade_label.pack(pady=10)

cidade_entry = tk.Entry(root, width=30)
cidade_entry.pack(pady=5)

buscar_button = tk.Button(root, text="Buscar Previsão", command=obter_previsao)
buscar_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 12), wraplength=250)
resultado_label.pack(pady=10)

root.mainloop()


#:V