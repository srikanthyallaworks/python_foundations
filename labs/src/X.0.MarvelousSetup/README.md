# McMullen's Marvelous Headless SBC Setup Recipe

## Summary

More broad strokes than a recipe, these are some steps to boot your 
SBC for the first time, secure it, and update the software. 

Skip any steps you've already completed.

Equipment:
  * 1 SBC - I have the Raspberry Pi 4
    + USB C cable
    + Wall wart 
  * 1 MiniSD imaged with [Raspberry Pi OS](https://www.raspberrypi.org/software/) 
  * Wifi network


## Product Requirements:
1. Configure WIFI credentials
2. Boot your SBC
3. Connect remotely via SSH
4. Setup
   a. Host name
   b. Login credentials
   c. Group membership
5. Update software



## Hints

### Configure Wifi
 
You'll need to edit the file `wpa_supplicant.conf` in the SD 
card `boot` directory. 

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

Details [here](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md).

### Boot up

Official guide [here](https://www.raspberrypi.org/documentation/remote-access/ip-address.md).

Alternatively, I use nmap on linux to find the IP address like this:

```
nmap 10.0.0.0/24
```

Results look like this:

> starting Nmap 7.80 ( https://nmap.org ) at 2021-01-22 04:48 MST
>
> Nmap scan report for 10.0.0.102
> Host is up (0.0091s latency).
> Not shown: 999 closed ports
> PORT   STATE SERVICE
> 22/tcp open  ssh
>
> ...
> 
> Nmap done: 256 IP addresses (5 hosts up) scanned in 12.41 seconds


### Connect remotely via SSH

Username: pi
Password: raspberry

Command: 
```
ssh 10.0.0.102 -l pi
```

### Create a new login
Good guide [here](https://www.raspberrypi.org/documentation/linux/usage/users.md).

```
sudo adduser jbloggs sudo spi
exit
```

Now connect as jbloggs and delete the default:

```
ssh 10.0.0.102 -l jbloggs
sudo userdel -r pi
```

### Rename the host
```
sudo hostname new-host
```

### Update Software

```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
```