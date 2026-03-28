import os
import time
import sys
import subprocess # Vamos usar subprocess para chamadas externas mais controladas

# --- Funções Auxiliares ---
def run_shell_command(command, cwd=None):
    """Executa um comando shell de forma segura e verifica erros."""
    try:
        # Usamos shell=True APENAS se o comando for uma string complexa com pipes, etc.
        # Caso contrário, é melhor passar como lista: ['bash', 'script.sh']
        subprocess.run(command, check=True, cwd=cwd, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"\033[1;31;40mErro ao executar comando: {command}\033[0m")
        print(f"\033[1;31;40mDetalhes do erro: {e.stderr}\033[0m")
    except FileNotFoundError:
        print(f"\033[1;31;40mComando ou script não encontrado: {command}\033[0m")

def display_logo():
    """Chama o script Logo.sh para exibir o logo."""
    run_shell_command(["bash", "Logo.sh"], cwd=os.path.expanduser("~/AllHackingTools"))

def display_menu_options():
    """Chama o script MenuOps.sh para exibir as opções do menu."""
    run_shell_command(["bash", "src/MenuOps.sh"], cwd=os.path.expanduser("~/AllHackingTools"))

def display_info_banner():
    """Chama o script Inf.sh para exibir o banner de informação."""
    run_shell_command(["bash", "src/Inf.sh"], cwd=os.path.expanduser("~/AllHackingTools"))
    time.sleep(0.3)

# --- Funções para os Sub-Menus (reimaginadas para Python 3) ---
# A ideia aqui é que, idealmente, essas seriam funções Python 3
# que você escreveria, ou módulos importados.
# Por enquanto, vamos simular a chamada dos antigos scripts Python 2
# mas já usando a abordagem mais controlada de subprocess.

def run_ip_menu():
    print("Executando módulo de IP (adaptado para Python 3)...")
    # Aqui, a gente chamaria o script Python 2, mas de forma mais segura.
    # O ideal é que o conteúdo de Files/IpMenu.py fosse reescrito em Python 3.
    # Por agora, mantemos a chamada ao python2 para compatibilidade temporária.
    run_shell_command(["python2", "Files/IpMenu.py"], cwd=os.path.expanduser("~/AllHackingTools"))

def run_router_menu():
    print("Executando módulo de Roteador (adaptado para Python 3)...")
    run_shell_command(["python2", "Files/RouterMenu.py"], cwd=os.path.expanduser("~/AllHackingTools"))

def run_mail_menu():
    print("Executando módulo de E-mail (adaptado para Python 3)...")
    run_shell_command(["python2", "Files/MailMenu.py"], cwd=os.path.expanduser("~/AllHackingTools"))

# --- Função Principal do Menu ---
def main_menu():
    os.system("clear") # Limpa a tela
    # Garante que estamos no diretório base do AllHackingTools
    # Importante para que os paths relativos funcionem
    all_hacking_tools_path = os.path.expanduser("~/AllHackingTools")
    os.chdir(all_hacking_tools_path)

    display_logo()
    display_menu_options()

    op = input("Options: ")

    if op == "1":
        display_info_banner()
        run_ip_menu()
    elif op == "2":
        display_info_banner()
        run_router_menu()
    elif op == "3":
        display_info_banner()
        run_mail_menu()
    # Continua adicionando as outras opções aqui, adaptando cada uma.
    # Por exemplo, para as opções de 4 a 20, a estrutura seria a mesma:
    # elif op == "4":
    #     display_info_banner()
    #     print("Executando módulo de Web (adaptado para Python 3)...")
    #     run_shell_command(["python2", "Files/WebMenu.py"], cwd=all_hacking_tools_path)

    elif op == "21":
        display_info_banner()
        os.system("clear") # Limpa a tela
        run_shell_command(["bash", ".settings/LICENSE.sh"], cwd=all_hacking_tools_path)
        run_shell_command(["python3", "src/Timer2.py"], cwd=all_hacking_tools_path)
        # Atenção aqui: o original chama python2 MainMenu.py, isso criaria um loop infinito
        # Se MainMenu.py já é python3, poderíamos simplesmente chamar main_menu() novamente
        # Ou reavaliar a lógica desse relançamento. Por enquanto, vou "simular" o relançamento.
        print("\033[1;33;40mReiniciando o sistema (simulado - reverter para main_menu() se for Python 3).\033[0m")
        time.sleep(2)
        main_menu() # Por enquanto, volta para o menu principal

    elif op == "22":
        display_info_banner()
        time.sleep(1)
        # O original clona um repo e executa um script bash. Mantemos isso.
        print("Iniciando atualização...")
        run_shell_command("cd $HOME && git clone https://github.com/mishakorzhik/AutoUpdateMyTools && cd AutoUpdateMyTools && bash AllHackingToolupdate.sh", cwd=os.path.expanduser("~"))

    elif op == "23":
        display_info_banner()
        run_shell_command(["bash", "src/About.sh"], cwd=all_hacking_tools_path)

    elif op == "13324715":
        print("[DEBUG] Developer mode successfully enabled!")
        time.sleep(0.8)
        # Comandos mv/cp para manipular arquivos.
        # Usamos subprocess para eles também, mas são mais complexos por serem múltiplos.
        # Idealmente, faríamos essas operações diretamente com o módulo 'shutil' do Python.
        print("[DEBUG] Movendo arquivos de configuração...")
        run_shell_command(f"mv .settings/DesingLogo.py {all_hacking_tools_path}/.temp/ && mv .settings/DesingMenu.py {all_hacking_tools_path}/.temp/", cwd=all_hacking_tools_path, shell=True)
        print("[DEBUG] Por favor, reinicie o AllHackingTools!")
        run_shell_command(f"mv MainMenu.py {all_hacking_tools_path}/.temp/temp && cp .settings/debug/MainMenu.py {all_hacking_tools_path}/", cwd=all_hacking_tools_path, shell=True)
        print("[DEBUG] Aviso! A personalização foi desativada.")
        time.sleep(3) # Dê um tempo para o usuário ler as mensagens de debug

    elif op == "24":
        os.system("clear")
        display_logo()
        print("\033[1;31;40mExiting System...\033[0m")
        time.sleep(0.7)
        sys.exit() # Sai do programa

    else:
        print("\033[1;31;40mEntrada inválida. Recarregando Ferramentas...\033[0m")
        time.sleep(1.6)
        main_menu() # Volta para o menu principal em vez de tentar reiniciar um script

if __name__ == "__main__":
    main_menu()
