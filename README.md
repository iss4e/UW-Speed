# speed-node-red
This project assumes you are using a Raspberry Pi 3 with the default configuration and
have access to the internet (either by wi-fi or ethernet).

**IMPORTANT: ensure that your RPi is connected to the electrical grid with the native power supply.**
Phone chargers do not provide sufficient power and, if you use one, you will see a yellow thunderbolt
warning icon in the upper right corner of your desktop.

* Update RPi firmware by running `sudo rpi-update`
* Update RPi software by running:
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
* Install npm:
```
sudo apt-get install npm
sudo npm install -g npm@2.x
hash -r
```

*SPEED-specific instructions begin*
* Run `cd ~/.node-red`

* Install project specific nodes:
  * MySQL: `npm install node-red-node-mysql`
  * A/D Converter: `npm install node-red-node-pi-mcp3008`

* Get the repository from github:
```
git init
git remote add origin https://github.com/iss4e/speed-node-red
git fetch
git reset origin/master
git checkout -t origin/master
```

* TODO: Set up MySQL database with the appropriate schema.

*SPEED-specific instructions end*

Using Node-RED:
* Use `node-red-start` to start Node-RED
* Go to `127.0.0.1:1880` in your browser to access Node-RED GUI:
  * **IMPORTANT: do not use Epiphany (the default RPi browser) for Node-RED GUI**
  * Use other browsers, such as Firefox
* Use `node-red-stop` to stop Node-RED
* Use `node-red-log` to view the recent log output
* Use `sudo systemctl enable nodered.service` to autostart Node-RED at every boot
* Use `sudo systemctl disable nodered.service` to disable autostart on boot
