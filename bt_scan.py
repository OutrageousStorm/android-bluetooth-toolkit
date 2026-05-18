#!/usr/bin/env python3
"""
bt_scan.py -- Scan for discoverable Bluetooth devices
Usage: python3 bt_scan.py [--timeout 10]
"""
import subprocess, time, re, argparse

def adb(cmd):
    r = subprocess.run(f"adb shell {cmd}", shell=True, capture_output=True, text=True)
    return r.stdout.strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=10, help="Scan timeout in seconds")
    args = parser.parse_args()

    print(f"\n🔵 Bluetooth Scanner — scanning for {args.timeout}s...\n")
    
    # Enable BT if off
    adb("settings put global bluetooth_on 1")
    time.sleep(1)
    
    # Start discovery
    adb("dumpsys bluetooth_manager | grep -i discovering || /system/bin/hcitool scan")
    
    # Wait for results
    time.sleep(args.timeout)
    
    # Get discovered devices
    out = adb("dumpsys bluetooth_manager | grep -A 5 'name='")
    
    print("Found devices:")
    if out:
        for line in out.splitlines():
            print(f"  {line}")
    else:
        print("  (no devices found)")

if __name__ == "__main__":
    main()
