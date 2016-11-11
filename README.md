# speed-node-red

**General RPi instructions**

This project assumes you are using a Raspberry Pi 3 with the default configuration and
have access to the internet (either by wi-fi or ethernet).

**IMPORTANT: ensure that your RPi is connected to the electrical grid with the native power supply.**
Phone chargers do not provide sufficient power and, if you use one, you will see a yellow thunderbolt
warning icon in the upper right corner of your desktop.

It might be a good idea to use a fresh SD card in order to prevent
any loss of data from previous projects and/or network and script conflicts.

You may download the OS installer to your SD card as explained on
the official [website](https://www.raspberrypi.org/downloads/noobs/).

If on campus, you may connect to `uw-wifi-setup-no-encryption` and download the configuration script for `eduroam`.
Run the script and use **project-specific credentials** to access `eduroam`.
**SECURITY NOTE: do not use your personal `eduroam` credentials, because they will be stored on the SD card in an unencrypted form.**
You might need to do some additional tweaking  of `wpa_supplicant` configuration files
and reboot the computer before the connection becomes available.

*Note: upgrading your system as shown below may take quite some time.*

* Upgrade RPi software by running:
```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install firefox-esr
```

* Upgrade RPi firmware by running `sudo rpi-update`

* Updgrade node.js and Node-RED by running `update-nodejs-and-nodered`
* Enable SPI:
  * Run `sudo raspi-config`
  * Select `Advanced Options`, select `A0 Update`
  * Select `Advanced Options`, select `SPI`
  * Select `yes` to enable SPI, select `OK` to confirm, select the `Finish` button
* Add yourself to the `spi` group: `sudo adduser pi spi`
* Reboot computer: `reboot`

**SPEED-specific instructions begin**

Install and configure additional software packages.
You will be prompted to to set up a MySQL password for user `root` during the installation.
You will use this password later in Node-RED editor.
```
sudo apt-get install python2.7-dev mysql-server mysql-client
mysql -uroot -p
CREATE DATABASE speed;
exit
```

* Get the repository from github:
```
cd
rm -rf .node-red
git clone --recursive https://github.com/iss4e/speed-node-red .node-red
cd .node-red/user_modules/MFRC522-python
git checkout master
cd
git clone https://github.com/lthiery/SPI-Py SPI-Py
cd SPI-Py
python setup.py install
cd
```

* Install project-specific nodes:
```
cd ~/.node-red
npm install node-red-node-mysql node-red-dashboard node-red-node-pi-mcp3008
```

**Using Node-RED**
* Use `node-red-start` to start Node-RED
* Use `node-red-stop` to stop Node-RED
* Use `node-red-log` to view the recent log output
* Use `sudo systemctl enable nodered.service` to autostart Node-RED at every boot
* Use `sudo systemctl disable nodered.service` to disable autostart on boot

**IMPORTANT: do not use Epiphany (the default RPi browser) to access Node-RED GUI; use other browsers, such as Iceweasel (Firefox)**
* Go to [localhost:1880](http://localhost:1880) in your browser to access Node-RED editor
  * Click on any orange node marked `speed` and enter your MySQL credentials for user `root`.
  * Re-deploy the flow afterwards.
* Go to [localhost:1880/main](http://localhost:1880/main) in your browser to access SPEED client GUI
* Go to [localhost:1880/ui](http://localhost:1880/ui) in your browser to access Node-RED dashboard for monitoring

*For more information on Node-RED go to the official [website](https://nodered.org/).*

**Using `git` in this project**

Unfortunately, Node-RED flow data is stored in a `flows_raspberrypi.json` file, which is not very suitable for collaborative editing.
Therefore, it is the most practical approach to avoid having two people editing the flow simultaneously on two different machines,
because the merging process would be very difficult.

If more than one person is going to work on the project, it would be acceptable to work in stages: one person finishes their work,
syncs the progress to this online repository, and lets the other person work on it.

The specific GIT instructions for this scenario would be the following.
You will be working within the `~/.node-red` folder.
* Use `git status` and `git log` for infromation purposes at any time
* Before your start work, make sure you are working with the most recent version of this repo: `git pull`
* After you modified some files locally, add them to the staging area: `git add -A` or `git add [specific file]`
* If you are ready to make a commit, run `git commit -m "[commit message]"`
* Once you are done working on your stage of the project, push your changes to this online repo: `git push`

For more information on git commands, use the web and `man git [command]`.
