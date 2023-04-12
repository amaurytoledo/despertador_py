import tkinter as tk
import datetime
import time
import winsound

class Despertador:
    def __init__(self, master):
        self.master = master
        master.title("Despertador")

        # Label com instrução
        self.instrucao_label = tk.Label(master, text="Defina o horário do alarme:")
        self.instrucao_label.pack()

        # Caixa de entrada para hora
        self.hora_var = tk.StringVar()
        self.instrucao_label = tk.Label(master, text="Horas:")
        self.instrucao_label.pack()
        self.hora_entry = tk.Entry(master, textvariable=self.hora_var, width=5)
        self.hora_entry.pack()

        # Caixa de entrada para minutos
        self.minutos_var = tk.StringVar()
        self.instrucao_label = tk.Label(master, text="Minutos:")
        self.instrucao_label.pack()
        self.minutos_entry = tk.Entry(master, textvariable=self.minutos_var, width=5)
        self.minutos_entry.pack()

        # Botão para definir alarme
        self.definir_botao = tk.Button(master, text="Definir", command=self.definir)
        self.definir_botao.pack()

        # Botão para parar alarme
        self.parar_botao = tk.Button(master, text="Parar", command=self.parar, state=tk.DISABLED)
        self.parar_botao.pack()

        self.alarme_definido = False

    def definir(self):
        hora = self.hora_var.get()
        minutos = self.minutos_var.get()

        try:
            hora = int(hora)
            minutos = int(minutos)
        except ValueError:
            tk.messagebox.showwarning("Erro", "Hora ou minutos inválidos")
            return

        agora = datetime.datetime.now()
        alarme = agora.replace(hour=hora, minute=minutos, second=0, microsecond=0)
        if alarme < agora:
            alarme += datetime.timedelta(days=1)

        diferenca = alarme - agora
        segundos = diferenca.total_seconds()

        self.hora_entry.config(state=tk.DISABLED)
        self.minutos_entry.config(state=tk.DISABLED)
        self.definir_botao.config(state=tk.DISABLED)
        self.parar_botao.config(state=tk.NORMAL)
        self.alarme_definido = True

        time.sleep(segundos)
        if self.alarme_definido:
            self.toque()

    def toque(self):
        while self.alarme_definido:
            winsound.Beep(1000, 1000)

    def parar(self):
        self.alarme_definido = False
        self.hora_entry.config(state=tk.NORMAL)
        self.minutos_entry.config(state=tk.NORMAL)
        self.definir_botao.config(state=tk.NORMAL)
        self.parar_botao.config(state=tk.DISABLED)


root = tk.Tk()
despertador = Despertador(root)
root.mainloop()
