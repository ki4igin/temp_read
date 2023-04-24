import serial
from serial.tools.list_ports import comports

ser = serial.Serial(timeout=0.5)

for port in sorted(comports()):
    print(f"Попытка найти устройство на порту {port.name}")
    ser.port = port.name
    try:
        ser.open()
    except serial.SerialException as e:
        print(e)
        continue
    rx = ser.read(1)
    ser.close()
    if len(rx) > 0:
        break
else:
    print('Устройство не найдено')
    exit(1)
