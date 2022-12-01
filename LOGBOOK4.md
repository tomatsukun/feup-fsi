#Tarefas Realizadas na Semana #4

##CTF

###Challenge 1

This Challenge required a lot of exploration and search. First we tried to find errors in the website, then we discovered some useful information about versions:
-Wordpress - 5.8.1
-WooCommerce plugin - 5.7.1
-Booster for WooCommerce plugin - 5.4.3
We used this information to try to find a CVE that matched that information and that would allow us to login as an admin. We managed to find the CVE with id CVE-2021-34646, that matched the restrictions (https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34646), so the correct flag we submited was flag{CVE-2021-34646}.

###Challenge 2

In This Challenge, we first started by going into exploit Database to try and find the exploit that would help us login as an admin. We managed to find one exploit with the CVE we found in challenge 1 (https://www.exploit-db.com/exploits/50299). This exploit was written in a python script that when given the URL and user_id we wanted (in this case we wanted to login as admin which had the user id 1), It would give us some links to the website that could've let us immediately login as the user with with the given user id. After login in as an admin we went to section with the private posts and found the flag in a post with the title "Message to our employees". This flag was flag{please don't bother me}.

![](https://i.imgur.com/MzGNbmK.png)

##Tarefas

###Tarefa 1

After using the command printenv , all the enviroment variables were printed to the terminal and using the command printenv <env> allowed us to single one only one variable since there are multiple enviroment variables. The commands export and unset were used by to us to set a fictional enviroment variable "abc" with the value "bla2" and delete It afterwards.

![](https://i.imgur.com/WfRY0iO.png)
![](https://i.imgur.com/RQ5n0wM.png)

###Tarefa 2

We compiled and run the program myprintenv.c. Then We commented the printenv() statement in the child process and uncommented the printenv() statement in the parent process. After compiling and running the for the second time we noticed there was no differences between the two.

![](https://i.imgur.com/kOTnSM5.png)

###Tarefa 3

When calling execve without the environ variable the result we get is a blank file which means the envrironment variables were not passed.
On the opposite, if we change the call to one using the environ variable we get a file with all environment variables with a result similar to the one in "Tarefa 1".

![](https://i.imgur.com/HkvKkMc.png)

###Tarefa 4

Since the system() function executes a program via the shell all the enviroment variables of the calling process are passed to new program. The output of the program are all the enviroment variables of the calling process that were passed to the program.

![](https://i.imgur.com/sQglqKg.png)

###Tarefa 5

After compiling and running the program with ownership to root and the program without that ownership we verified that there was no differences in output. So all enviroment variable set in the shell process got into the Set-UID child process.

![](https://i.imgur.com/qYuXb3K.png)

###Tarefa 6

In this task we exploit the use of `system()` in the following `target.c`  program which depends on the environment variables.
```c
#include <stdlib.h>

int main(){
    system("ls");
    return 0;
}
```

As the `system` argument was not a **full path** it will search the *ls* executable in the `$PATH` environment variable
so if we alter the path we can alter what program it will execute!

```bash
export PATH=/home/seed/setuid:$PATH
```

Were we changed our `$PATH` to look for in our current directory, the one where the mallicious ls will be.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
  printf("You have been hacked!\n");
  if (getuid() == 0)
    printf("You have root privileges\n");
  else 
    printf("You are a user\n");
  return 0;
}
```

Here we can see how we've stolen the control of that program to run our code!
![](./imgs/malliciousLs1.png)

If we set the owner of that executable `target` to root and make it a `Set-Uid`
program we will be able to gain root privileges!

![](./imgs/malliciousLs2.png)

Something we learned with this task:
- `getuid()` returns the real user ID of the calling process.
- `geteuid()` returns the effective user ID of the calling process.

The *UID* indicates the actual user who is performing the action. 
The *EUID* is the effective user id and it is what we change when we run a `Set-UID` program


