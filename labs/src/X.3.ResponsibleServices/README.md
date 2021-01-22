# Responsible Services

## Summary

Unattended upgrades involves tradeoffs. On the one hand, 
you don't have to remember to apply security patches. But
they might break something too. 

So maybe it's a good approach for your internet router,
but not appropriate for the software running a nuclear 
power plant.


## Product Requirements:
1. Decide if you want automatic updates, if you do ...
2. Decide on a mechanism
3. Make it so!


## Hints

I like Debian's package [Unattended Upgrades](https://wiki.debian.org/UnattendedUpgrades)

It's worked out for me.

Here's how to install:
```
sudo apt-get update
sudo apt-get install unattended-upgrades apt-listchanges
```

To activate and configure, follow instructions here:
   https://wiki.debian.org/UnattendedUpgrades

## Resources

* Here's an alternative approach using a chron job:
   https://www.raspberrypi.org/forums/viewtopic.php?t=111794

