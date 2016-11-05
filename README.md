# speed-node-red
This project assumes you are using a Raspberry Pi 3 with the default configuration and
have access to the internet (either by wi-fi or ethernet).
**SECURITY NOTE:** do not store your personal credentials for wi-fi authentication on the Pi; use project-specific credentials instead.

**IMPORTANT: ensure that your RPi is connected to the electrical grid with the native power supply.**
Phone chargers do not provide sufficient power and, if you use one, you will see a yellow thunderbolt
warning icon in the upper right corner of your desktop.

**General RPi instructions**
* Upgrade RPi firmware by running `sudo rpi-update`
* Upgrade RPi software by running:
```
sudo apt-get update
sudo apt-get dist-upgrade
```

* Updgrade node.js and Node-RED by running ``update-nodejs-and-nodered``
* Enable SPI:
  * Run `sudo raspi-config`
  * Select `Advanced Options`, select `A0 Update`
  * Select `Advanced Options`, select `SPI`
  * Select `yes` to enable SPI, select `OK` to confirm, select the `Finish` button
* Add yourself to the `spi` group: `sudo adduser pi spi`
* Reboot computer: `reboot`

**SPEED-specific instructions begin**

* Get the repository from github:
```
cd
rm -rf .node-red
git clone --recursive https://github.com/iss4e/speed-node-red .node-red
cd .node-red/user_modules/MFRC522-python
git checkout master
```

* Install project-specific nodes:
```
cd ~/.node-red
npm install node-red-node-mysql
npm install node-red-node-pi-mcp3008
```

* *TODO: Set up MySQL database with the appropriate schema.*

**SPEED-specific instructions end**

**Using Node-RED**
* Use `node-red-start` to start Node-RED
* Go to `127.0.0.1:1880` in your browser to access Node-RED GUI:
  * **IMPORTANT: do not use Epiphany (the default RPi browser) for Node-RED GUI**
  * Use other browsers, such as Firefox
* Use `node-red-stop` to stop Node-RED
* Use `node-red-log` to view the recent log output
* Use `sudo systemctl enable nodered.service` to autostart Node-RED at every boot
* Use `sudo systemctl disable nodered.service` to disable autostart on boot
