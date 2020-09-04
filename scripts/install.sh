#!/bin/bash

cp rax30_lircd.conf /etc/lirc/lircd.conf.d/rax30.lircd.conf

SERVICE_NAME="IRReceiverController"

echo "Installing systemd service"

rm -rf /usr/local/lib/$SERVICE_NAME
cp -rp ./src /usr/local/lib/$SERVICE_NAME
chown -R root:root /usr/local/lib/$SERVICE_NAME

rm /etc/systemd/system/$SERVICE_NAME.service
cp $SERVICE_NAME.service /etc/systemd/system/
chown root:root /etc/systemd/system/$SERVICE_NAME.service
chmod 644 /etc/systemd/system/$SERVICE_NAME.service

systemctl stop $SERVICE_NAME
systemctl enable $SERVICE_NAME
systemctl daemon-reload
systemctl start $SERVICE_NAME
