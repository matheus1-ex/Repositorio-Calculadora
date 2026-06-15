def calculadora(n1, n2, operador):
	while (n1, n2):
		match operador:
			case "+":
				soma = n1 + n2
				print(soma)
			case "-":
				sub = n1 - n2
				print(sub)
			case "/":
				div = n1 / n2
				print(div)
			case "*":
				mult = n1 * n2
				print(mult)
			case " ":
				print("ERROR!!!")
		break

start = True
while start != "del":
	start = input("Digite (start) para começar e (del) para sair: ").strip().upper()
	if start == "DEL":
		break
	if start not in ("DEL", "START"):
		print("PEENN! Inválido")
		while start not in ("del", "start"):
			start = input("Digite (start) para começar e (del) para sair: ")
	if start:
		num1 = float(input("Digite um número: "))
		num2 = float(input("Digite outro número: "))
		op = str(input("Digite o operador: "))
		calculadora(num1, num2, op)
	continuar = input("Deseja continuar? (S/N): ").strip().upper()[0]
	while continuar not in ("S", "N"):
		continuar = input("Deseja continuar? (S/N): ").strip().upper()[0]
	if continuar == "N":
		break
	
	