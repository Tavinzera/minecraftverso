import os
import json
import subprocess
import time

# Caminhos usando o BASE_DIR fornecido pelo update.py
# Se o BASE_DIR não vier, usamos o caminho relativo
try:
    path_to_bin = os.path.join(BASE_DIR, "bin")
    path_to_config = os.path.join(BASE_DIR, "config", "version.json")
except:
    path_to_bin = "bin"
    path_to_config = "config/version.json"

hello_file = os.path.join(path_to_bin, "aviso.txt")

hello_text = """
============================================================
              POKEVERSE - ATUALIZACAO CONCLUIDA             
============================================================

   _    _      _ _         __          __           _     
  | |  | |    | | |        \ \        / /          | |    
  | |__| | ___| | | ___     \ \  /\  / /__  _ __ __| |    
  |  __  |/ _ \ | |/ _ \     \ \/  \/ / _ \| '__/ _` |    
  | |  | |  __/ | | (_) |     \  /\  / (_) | | | (_| |    
  |_|  |_|\___|_|_|\___/       \/  \/ \___/|_|  \__,_|    
                                                          
============================================================
 FECHE ESTE BLOCO DE NOTAS PARA INICIAR O SEU MINECRAFT!
============================================================
"""

try:
    # 1. Criar o ficheiro de texto
    with open(hello_file, "w", encoding="utf-8") as f:
        f.write(hello_text)
    
    # 2. Tentar abrir o Notepad de forma robusta
    # Usamos o start para não travar o processo dependendo da configuração
    os.system(f'notepad.exe "{hello_file}"')
    
    # Damos um pequeno tempo para o Windows processar
    time.sleep(1)

except Exception as e:
    print(f"Erro ao abrir aviso: {e}")

# 3. Atualizar a versão para o Launcher não repetir o processo
try:
    nova_versao = {"version": "1.0.1"} # Mude para a versão do site
    with open(path_to_config, "w") as f:
        json.dump(nova_versao, f)
except:
    pass
