#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.publish as publish

HOST = "192.168.1.188"

publish.single("sensor", "payload", hostname=HOST)