#!/usr/bin/env python3
import requests
import subprocess
import os
import json
from datetime import datetime

# Insira sua chave de API aqui:
api_key = "7e76dbf642e7f3197e30bfb3b55e8e0d7a46197ab3d85d46909c3c7b0530e165"
url = "https://c137.belini.shop/api/generateText"

# Inicializa a lista de respostas anteriores
respostas_anteriores = []

def rewrite_api_key():
    global api_key
    api_key_rewrited = False
    while not api_key:
        api_key = input("Digite a sua chave de API: ")
        try:
            # Verifica se a chave de API é válida
            data = {
                "key": api_key,
                "text": "Teste",
                "model_name": "c137_uncensored",
                "instructions": "Teste"
            }
            response = requests.post(url, data=data)
            if response.status_code != 200:
                raise Exception("Chave de API inválida")
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
    global respostas_anteriores
    kernel = subprocess.check_output(["uname", "-r"]).decode("utf-8").strip()
    path = os.getcwd()

    # Adiciona as respostas anteriores ao prompt
    prompt_com_respostas = f"prompt atual: {prompt}\n{' comandos anteriores já feitos: '.join(respostas_anteriores)}"
    instructions = f"""Gere um comando shell puro para o seguinte prompt:
Prompt: {prompt_com_respostas}
Kernel: {kernel}
Diretório atual: {path}"""

    try:
        data = {
            "key": api_key,
            "text": prompt,
            "model_name": "c137_uncensored",
            "instructions": instructions
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            response_json = response.json()
            generated_text = response_json.get("generated_text", "")
            # Extrair apenas o comando puro
            command = generated_text.strip().strip('```bash').strip('```').strip()
            # Adiciona a resposta atual às respostas anteriores
            respostas_anteriores.append(command)
            return command
        else:
            raise Exception(f"Erro na API: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu uma exceção ao chamar a API: {e}")
        return None

# Função para gerar uma descrição detalhada do comando gerado
def command_description(prompt):
    instructions = f"""Gere uma descrição detalhada sobre esse comando shell:
    comando: {prompt}"""
    try:
        data = {
            "key": api_key,
            "text": prompt,
            "model_name": "c137_uncensored",
            "instructions": instructions
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            response_json = response.json()
            generated_text = response_json.get("generated_text", "")
            # Extrair apenas a descrição pura
            description = generated_text.strip().strip('```bash').strip('```').strip()
            return description
        else:
            raise Exception(f"Erro na API: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu uma exceção ao chamar a API: {e}")
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
            print("Opções:\n 1-Aplicar comando na minha máquina\n 2-Descrever detalhadamente o que esse comando faz \n 3-Ir para o próximo comando\n 4-Mudar api_key")
            print(divider)
            confirm = input("Escolha uma opção (1, 2, 3 ou 4): ")
            print(divider)
            if confirm == "1":
                subprocess.run(command, shell=True)
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
                print("Comando errado, nada foi feito, tente novamente")
                continue
            print(divider)

start_app()

