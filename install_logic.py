import os
import json

# Exemplo: Atualizar o ficheiro local para que o launcher saiba que já atualizou
config_path = os.path.join(os.getcwd(), "config", "version.json")
nova_versao = {"version": "1.0.1"} # Pega isto do teu sistema

with open(config_path, "w") as f:
    json.dump(nova_versao, f)

print("Versão local atualizada!")
# Aqui adicionarias o código para descarregar os .jar dos mods
