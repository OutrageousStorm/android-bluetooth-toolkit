# 🔵 Android Bluetooth Toolkit

Monitor, control, and debug Bluetooth devices on Android.

## Scripts

| Script | What it does |
|--------|-------------|
| `bt_scan.py` | Scan for discoverable devices |
| `bt_monitor.py` | Watch connected device signal strength |
| `bt_battery.py` | Monitor paired device battery levels |
| `bt_pair.py` | Pair/unpair devices interactively |
| `bt_debug.sh` | Enable Bluetooth debugging logs |

## Quick start

```bash
# Scan for nearby devices
python3 bt_scan.py

# Show battery level of all paired devices
python3 bt_battery.py

# Monitor connection strength of a device
python3 bt_monitor.py --device "Pixel Buds"
```
