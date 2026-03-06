import os
import json
import subprocess

# 1. Caminhos
base_dir = os.getcwd()
config_path = os.path.join(base_dir, "config", "version.json")
hello_file = os.path.join(base_dir, "bin", "hello.txt")

# 2. Texto "Hello World" Grande (ASCII Art)
hello_text = """
############################################################
#                                                          #
#   _    _      _ _         __          __           _     #
#  | |  | |    | | |        \ \        / /          | |    #
#  | |__| | ___| | | ___     \ \  /\  / /__  _ __ __| |    #
#  |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__/ _` |    #
#  | |  | |  __/ | | (_) |     \  /\  / (_) | | | (_| |    #
#  |_|  |_|\___|_|_|\___/       \/  \/ \___/|_|  \__,_|    #
#                                                          #
#                                                          #
############################################################
"""

# 3. Criar o arquivo de texto e abrir o Notepad
try:
    with open(hello_file, "w") as f:
        f.write(hello_text)
    
    # Abre o notepad e ESPERA ele ser fechado para continuar (opcional)
    # Se quiser que o launcher continue só depois de fechar o bloco de notas, use .run
    # Se quiser que abra e continue na hora, use .Popen
    subprocess.run(["notepad.exe", hello_file])
    
    # Remover o arquivo após fechar (opcional)
    if os.path.exists(hello_file):
        os.remove(hello_file)
except Exception as e:
    print(f"Erro ao abrir notepad: {e}")

# 4. Atualizar a Versão Local para o Launcher saber que acabou
nova_versao = {"version": "1.0.1"} # Mude para a versão atual do seu Github
with open(config_path, "w") as f:
    json.dump(nova_versao, f)

print("Lógica concluída!")
