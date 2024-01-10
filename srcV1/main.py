#!pip install frida
#import frida as frd 
#import frida_tools as frdT
#frida nao esta em uso nessa versao: versao apenas de testes!!!!!!!!


import frida

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] Received message:", message['payload'])
    else:
        print("[*] Message type not recognized")

# Especifique o processo-alvo ou o caminho para o executável
target_process = "C:\XboxGames\Among Us\Content\Among Us.exe"

# Carregue o script de Frida
with open("src.js", "r") as script_file:
    script_code = script_file.read()

# Conecte-se ao processo alvo
session = frida.attach(target_process)

# Compile e injete o script
script = session.create_script(script_code)
script.on('message', on_message)
script.load()

# Mantenha a sessão ativa (pode adicionar lógica para esperar eventos)
frida.resume(target_process)

# Aguarde a interação ou pressione Ctrl+C para encerrar
try:
    input("[!] Pressione Enter para encerrar...\n")
except KeyboardInterrupt:
    pass
script_file.close()