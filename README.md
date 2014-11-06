pydd
====

Pydd it's a wrapper using the command dd Linux written in Python and using to viewer the progress of work.

-----------
Basic usage
-----------

The secret is to pass only the parameters of the dd command and run as root.

-------
Example
-------

user1@my_notebook ~ $ sudo python pydd.py

        Pydd:  Um wrapper do comando dd do Linux com visualização do progresso em Python
    
    ******************
        OBS: Não é necessario entra com dd, /bin/dd ou outro caminho do binario dd
    ******************
    ******************
        Exemplo: if=/home/user/image/rootfs.img of=/dev/sdc bs=512k
    ******************
    Entre com os parametros: if=/tmp/zImage.bin of=/dev/sdb
    ******************
    ******************
    Comando + parametros: ['/bin/dd', 'if=/tmp/zImage.bin', 'of=/dev/sdb']
    ******************
    ******************
    PID: 8250
    ******************
    Gravando: (537MB)       Tempo decorrido: 42,09s     Taxa: 35MB/s
