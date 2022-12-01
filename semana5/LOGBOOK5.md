## LOOGBOOK5


### Task 0: Environment Setup

- Primeiro usamos o comando "sudo sysctl -w kernel.randomize_va_space=0" para desativar a randomização do inicio dos endereços da "heap" e da "stack".


![](adressrandomizer.jpg)


### Task 1: Getting Familiar with Shellcode

- Depois de compilarmos o Makefile presente na pasta "shellcode"
e corrermos o programa obtemos o seguinte: 

![](a64.jpg)


### Task 2: Understanding the Vulnerable Program

- Rodamos este código "gcc -DBUF_SIZE=100 -m32 -o stack -z execstack -fno-stack-protector stack.c" para compilar o "stack.c" com a StackGuard  e "non-executable stack protections" desligados 
- Usamos "sudo chown root stack " para mudar a ownership do programa para a root
- Usamos "sudo chmod 4755 stack" para ligar o "SET-UID"

![](task2.1.jpg)

### Task 3: Launching Attack on 32-bit Program (Level 1)

- Rodando o seguinte código:

![](code.jpg)

- Obtemos:

![](ebpebuffer.jpg)

- Explicando o ataque:

1. Ingetamos a versão de 32 bits do shellcode
2. Inicializamos o ficheiro todo com NOPs 
3. Colocamos o código malicioso no final do payload
4. Com a informação que obtemos do "ebp" e "buffer" podemos criar um endereço suficientemente grande onde queremos retornar para encontrar os NOPs que nos levam ao shellcode


![](final.jpg)