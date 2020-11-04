Title: Automate SSH login without password  
Date: 2020-10-25 12:00
Category: Linux
Slug: add_ssh_key

Generate key for remote host

```bash
ssh-keygen -t rsa -b 2048
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
```

Copy on remote host

```bash
ssh-copy-id username@server_ip
```
Enter password to access

```bash
username@server_ip password: 
```

Logging on ssh without password 

```bash
ssh username@server_ip
```