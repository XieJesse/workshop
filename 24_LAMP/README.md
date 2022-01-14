# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: _

### Prerequisites:

- Digital Ocean account verified and set up
-

1. Navigate to the control panel in digital ocean.
2. Select the "create" and the "droplet" button.
3. When prompted in the "select an image" section, select the ubuntu image (20.04.3).
4. In the "choose a plan" section, select all of the regular options and decline all optional settings.
5. In the "choose a datacenter region" section, select a datacenter located as close to New York as possible, if not in New York.
6. In the "authentication" section, select SSH keys.
7. To set up SSH keys for the droplet, on each machine that ssh keys are desired on, run ssh-keygen on each machine that you want SSH keys on.
8. After generating SSH keys, cat the file that the public SSH key is contained in and copy and paste the contents into the box that appears when you press "new SSH key" on digital ocean.
9. Repeat for each machine that you want SSH keys on.
10. Finalize the creation of the droplet by selecting any additional (free) options that you desire.
11. Celebrate the creation of your droplet that runs ubuntu!
12. To install apache onto the droplet, first ssh into the droplet by running $ ssh root@[idAddress].
13. Then run $ sudo apt update and $ sudo apt install apache2 to install it.
13. To allow users to connect to your web port(s), run $ sudo ufw allow 'Apache'.
14. Verify that your web server is active with $ sudo systemctl status apache2.
15. Your web server should be fully operational, as you can check by heading to the ip address of your droplet on any browser.
16. Celebrate getting apache web servers working on your droplet!

### Additional Steps:

- 


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-18-04-quickstart
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/

(please verify ; some of these are old links)

---

Accurate as of (last update): 2022-01-14

#### Contributors:  
Clyde "Thluffy" Sinclair  
Topher Mykolyk, pd0
Jesse Xie, pd2  
