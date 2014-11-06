#-*- coding: utf-8 -*-

import subprocess
import shlex
import signal
import os
import sys
import time
import re


def add_line(caractere,valor_mult):
    """
        Funcao para adicionar uma nova linha com caractere informado x o valor especificado, sendo
        uma linha para melhor formatação e visualização
    """
    print >>sys.stderr, caractere * valor_mult


def msg(action,message):
    """
        Função para printar mensagens personalizadas na tela
    """
    print >>sys.stderr, " " * 3, "\033[1;31m"+action+"\033[0m",message


def check_user():
    """ 
        Verifica se o usuario possui permissao de root(super-usuario)
    """
    if os.geteuid() != 0:
        add_line("*",20)
        msg("Erro:","O programa deve ser executado super-usuario!")
        add_line("*",20)
        sys.exit()

def cmd_dd(cmd):
    """
        Executa o comando dd com seus parametros e envia o sinal USR1 para capturar
        as informações do processo dd, manipula esta saida e printa o andamento na
        tela
    """
    my_proc = subprocess.Popen(cmd, shell=False, stderr=subprocess.PIPE, executable=None, creationflags=0)
    add_line("*",20)
    msg("PID: ",my_proc.pid)
    add_line("*",20)

    try:
        while my_proc.poll() is None:  
            time.sleep(.5)
            my_proc.send_signal(signal.SIGUSR1)
            while 1:
                my_proc_output = my_proc.stderr.readline()
                if 'bytes' in my_proc_output:
                    output_dd_list = my_proc_output.split()
                    print 'Gravado: ', output_dd_list[2]+output_dd_list[3],\
                        '\tTempo decorrido: ', output_dd_list[5]+output_dd_list[6],\
                        '\tTaxa: ', output_dd_list[7]+output_dd_list[8], '\r',
                    break

        print 'Gravado: ', output_dd_list[2]+output_dd_list[3],\
            '\tTempo decorrido: ', output_dd_list[5]+output_dd_list[6],\
            '\tTaxa: ', output_dd_list[7]+output_dd_list[8]

    except ValueError as ex_value:
        print("Erro: %s") % (ex_value)
        my_proc.terminate()
        my_proc.kill()
        exit()
    except KeyboardInterrupt:
        my_proc.terminate()
        my_proc.kill()
        sys.exit()


def main():
    try:
        add_line(" ",20)
        msg("Pydd :\t", "Um wrapper do commando dd do Linux com visualização do progresso em Python")
        add_line("",20)

        add_line("*",20) 
        msg("OBS:", "Não é necessario entrar com dd, /bin/dd ou outro caminho do binario dd")
        add_line("*",20) 
        
        add_line("*",20) 
        msg("Exemplo:", "if=/home/user/image/rootfs.img of=/dev/sdc bs=512k")
        add_line("*",20) 
        
        cmd_line = raw_input("Entre com o comando: ")
        cmd_params = shlex.split(cmd_line)
        
        check_user()

        """
            Não precisa passar o binario dd como parametro, mas caso o operador passe
            via expressão regular verifico e caso encontre é substituido por /bin/dd
            ou caso não seja passado é adicionado ao indice 0 da list o /bin/dd
        """
        if re.search('(^dd|dd$)',cmd_params[0]):
            cmd_params[0] = "/bin/dd"
        else:
            cmd_params.insert(0,"/bin/dd")

        add_line("*",20) 
        msg("Comando + paramentos: ", cmd_params)
        add_line("*",20) 
        
        cmd_dd(cmd_params)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
