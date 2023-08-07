#!/bin/bash
BATTERY_PATH=$(upower -e | grep 'BAT')
BATTERY_INFO=$(upower -i $BATTERY_PATH | grep -E 'state\|percentage')
echo $BATTERY_INFO
