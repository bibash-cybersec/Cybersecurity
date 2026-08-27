### See all users
  cat /etc/passwd

### Switch user
  su username

### Userinfo
  id username
  finger username 
  getent passwd username

### Add new user 
  sudo useradd -m -s /bin/bash newuser
  -m = create home directory
  -s = set default shell

### Set password to newly created user
  sudo passwd newuser

### Delete user
  sudo userdel -r username
  -r = remove home directory too

### Lock/Unlock account
  sudo usermod -L username -- Lock
  sudo usermid -U username -- Unlock

### Group Management

### See all groups
  cat /etc/group

### Create group
  sudo groupadd groupname

### Add user to group
  sudo usermod -aG groupname username
  sudo gpasswd -a username groupname 

### Remove user from group
  sudo gpasswd -d username groupname

### Delete group
  sudo groupdel groupname

**Important Groups**
  sudo - can run sudo cmd
  root - superuser group
  www-data - web server user
  shadow - can read /etc/shadow
  docker - can run docker( basically root)

  ### User information 
     root:x:0:0:root:/root:/bin/bash
      |   |  |  |   |      |        |______default shell
      |   |  |  |   |      |_______________home directory
      |   |  |  |   |______________________comment info
      |   |  |  |__________________________GUID
      |   |  |_____________________________UID
      |   |________________________________password in shadow
      |____________________________________username
    
