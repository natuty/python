#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.publish as publish

HOST = "192.168.1.199"

publish.single("sensor", "payload", hostname=HOST)