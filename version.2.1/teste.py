import customtkinter as CTk

janela = CTk.CTk()


class aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.main()
        janela.mainloop()

    def tela(self):
        janela.geometry("600x500")
        janela.title("CTk example")

    def main(self):
        button = CTk.CTkButton(self, command=lambda: button_click)
        button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
        def button_click():
            print("button click")


aplication()