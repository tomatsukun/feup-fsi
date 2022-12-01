# LOGBOOK8


## Task 1: Get Familiar with SQL Statements










## CTF 8





## Challenge 1

- The first challenge is a white box attack since the source code is available for analysis.

![](/images/ctf-query-vscode.jpg)

- Since there is no input sanitization we can easily exploit this.

- The username to be used in the challenge is provided by the challenge guide on moodle. Without this information, we would need to architecture a more general attack that would allow us to bypass not only the value of the password but also the username value.

- We can bypass authentication of the admin username by performing a SQL Injection. Exploiting the point that we mentioned earlier


```php
username: admin
password: ' OR ''=' 
```

- After we try to login with this credentials we obtain the flag.

![](/images/ctf-desafio1-flag.jpg)



## Challenge 2