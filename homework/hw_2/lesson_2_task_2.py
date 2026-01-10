from smartphone import Smartphone

device = Smartphone("Google", "Pixel", "+17343892398")
print(device.brand + " - " + device.model + ", " + device.phone_number)
print(device.brand, "-", device.model + ",", device.phone_number)
print(f"{device.brand} - {device.model}, {device.phone_number}")