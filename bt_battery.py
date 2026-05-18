#!/usr/bin/env python3
"""
bt_battery.py -- Show battery level of all paired Bluetooth devices
Usage: python3 bt_battery.py
"""
import subprocess, re

def adb(cmd):
    r = subprocess.run(f"adb shell {cmd}", shell=True, capture_output=True, text=True)
    return r.stdout.strip()

def main():
    print("\n🔋 Bluetooth Device Batteries\n")
    
    # Get all paired devices
    out = adb("settings get global bluetooth_devices_bonded")
    paired = adb("dumpsys bluetooth_manager | grep 'name='")
    
    # Get battery info
    battery = adb("dumpsys battery | grep -E 'level|temp'")
    
    # Get BT device battery (Android 5.0+)
    bt_battery = adb("dumpsys bluetooth_manager | grep -i 'battery'")
    
    print("Paired devices:")
    if paired:
        for line in paired.splitlines()[:10]:
            print(f"  {line}")
    
    if bt_battery:
        print("\nBattery levels:")
        print(bt_battery)
    else:
        print("\n(Battery info not available on this device)")

if __name__ == "__main__":
    main()
