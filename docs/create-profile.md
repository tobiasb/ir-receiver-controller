# How to create a profile

I mostly followed [this](https://www.instructables.com/id/Creating-a-Raspberry-Pi-Universal-Remote-With-LIRC/) tutorial , ecept for step 3 which isn't valid for Raspbian Buster anymore. Instead, do the following:

Configure `gpio-ir` for "receiving" mode.
```
sudo vi /boot/config.txt

#dtoverlay=gpio-ir-tx,gpio_pin=18
dtoverlay=gpio-ir,gpio_pin=18

sudo shutdown -r now
```

Stop LIRC service

```
sudo systemctl stop lircd
```

Test your setup

```
mode2 -d /dev/lirc0
```

Point your remote to the IR receiver and press a few buttons, you should see output similar to this:

```
...
pulse 541
space 575
pulse 631
space 495
pulse 566
space 541
pulse 572
space 548
pulse 602
space 1627
pulse 574
space 560
pulse 566
space 532
pulse 600
space 41407
pulse 9063
space 2192
pulse 593
pulse 128920
...
```

If so, start recording:

```
irrecord -d /dev/lirc0 ~/lircd.conf
```

Finally, move your configuration to where `lircd` can find it

```
sudo mv ~/lircd.conf /etc/lirc/lircd.conf.d/<your device model>.conf
```
