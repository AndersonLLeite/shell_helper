#!/usr/bin/env python3
import openai
import subprocess
import os

# Insira sua chave de API aqui:
api_key = ""

def rewrite_api_key():
    global api_key
    api_key_rewrited = False
    while not api_key:
        api_key = input("Digite a sua chave de API: ")
        try:
            # Verifica se a chave de API é válida
            openai.api_key = api_key
            openai.Completion.create(engine="text-davinci-002", prompt="Teste")
        except Exception as e:
            print(f"Chave de API inválida: {e}")
            api_key = ""
    with open(__file__, "r") as f:
        lines = f.readlines()
    with open(__file__, "w") as f:
        for line in lines:
            if "api_key =" in line:
            	if api_key_rewrited:
            		f.write(line)
            	else:
                	f.write(f"api_key = \"{api_key}\"\n")
                	api_key_rewrited = True
            else:
                f.write(line)

# Reescreve a chave de API no arquivo se ela estiver vazia
if not api_key:
    rewrite_api_key()

divider = "---------------------------------------------------------------------------- \n"

# Função para gerar o comando shell a partir do prompt em linguagem natural
def prompt_to_shell(prompt):
    kernel = subprocess.check_output(["uname", "-r"]).decode("utf-8").strip()
    path = os.getcwd()
    final_prompt = f"""Gere um comando shell a partir do seguinte prompt:

Prompt: {prompt}
Kernel: {kernel}
Diretório atual: {path}

Comando gerado:""".replace("\n", "")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=final_prompt.format(prompt=prompt),
            max_tokens=2000,
            api_key=api_key 
        )
        command = response.choices[0].text.strip()
        return command
    except Exception as e:
        print(f"Ocorreu uma exceção ao chamar a API da OpenAI: {e}")
        return None
    
# Função para gerar uma descrição detalhada do comando gerado
def command_description(prompt):
    kernel = subprocess.check_output(["uname", "-r"]).decode("utf-8").strip()
    path = os.getcwd()
    final_prompt = f"""Gere uma descrição detalhada sobre esse comando shell:
    comando:{prompt}"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=final_prompt.format(prompt=prompt),
            max_tokens=2000,
            api_key=api_key 
        )
        command = response.choices[0].text.strip()
        return command
    except Exception as e:
        print(f"Ocorreu uma exceção ao chamar a API da OpenAI: {e}")
        return None

def start_app():
	global api_key
	while True:
		print(divider)
		prompt = input("Digite um comando em linguagem natural (ou 'sair' para encerrar o programa):\n")
		print(divider)
		if prompt == 'sair':
			break
		command = prompt_to_shell(prompt)
		print(f"Comando gerado: {command}")
		
		
		
		# Pergunta ao usuário se ele deseja usar o comando gerado
		while True:
			print(divider)
			print("Opções:\n 1-Aplicar comando na minha máquina\n 2-Descrever detalhadamente o que esse comando faz \n 3-Ir para o próximo comando\n 4- Mudar api_key")
			print(divider)
			confirm = input("Escolha uma opção (1, 2, 3 ou 4): ")
			print(divider)
			if confirm == "1":
				command_without_prefix = command.replace("Comando gerado:", "").strip()
				subprocess.run(command_without_prefix, shell=True)
				print(divider)
				break
			elif confirm == "2":
				print(command_description(command))
				continue
			elif confirm == "3":
				break
			elif confirm == "4":
				api_key = ""
				rewrite_api_key()
				break
			else:
				print("Comando errado, nada foi feito, tente novamante")
				continue
			print(divider)

start_app()

