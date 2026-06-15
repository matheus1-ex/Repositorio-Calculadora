def abir_janela(tipo_janela, senha):
	if senha < 2:
		print("Senha Negativada!")
	else:
		print("Senha Válida!")

if __name__ == "__main__":
	abrir_janela(True, True)