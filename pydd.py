import subprocess
import shlex
import signal
import os
import sys
import time




def msg(action,message):
    print >>sys.stderr, "*" * 20
    print >>sys.stderr, "*" * 3, "\033[1;31m"+action+"\033[0m",message
    print >>sys.stderr, "*" * 20


def cmd_dd(cmd):
    my_proc = subprocess.Popen("/bin/dd "+cmd, shell=False, stderr=subprocess.PIPE, executable=None, creationflags=0)
    msg("PID: ",my_proc.pid)

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
        cmd_line = raw_input("Entre com o comando: ")
        cmd_params = shlex.split(cmd_line)
        msg("Comando + paramentos: ", cmd_params)
        cmd_dd(cmd_params)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
