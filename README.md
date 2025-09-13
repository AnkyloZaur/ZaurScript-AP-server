# ZaurScript AP Server for ESP8266

## English

This project provides a simple HTTP Access Point (AP) server for the ESP8266 (MicroPython) that serves `.zs` files from the device's flash memory. It is designed to work exclusively with (ZaurParser)[https://github.com/AnkyloZaur/ZaurParser "ZaurParser on GitHub"] running on Arduino UNO R4 Wifi, handling only requests compatible with ZaurParser.

### Features
- Sets up an open WiFi AP named `ZaurScript_AP` (can be password-protected)
- Serves `.zs` files (ZaurScript) stored in flash memory
- Compatible only with ZaurParser on UNO R4 Wifi
- If `main.zs` does not exist, it creates a default one

### Usage
1. Flash your ESP8266 with MicroPython.
2. Upload `zaurscript_ap_server.py` and `.zs` files to the ESP8266.
3. Run the script on the ESP8266.
4. Connect to the `ZaurScript_AP` WiFi network using ZaurParser device.
5. ZaurParser on UNO R4 Wifi can now request `.zs` files from the ESP8266 AP server.

---

## Polski

Ten projekt to prosty serwer HTTP w trybie Access Point (AP) dla ESP8266 (MicroPython), który udostępnia pliki `.zs` z pamięci flash urządzenia. Serwer obsługuje wyłącznie żądania kompatybilne z ZaurParserem na Arduino UNO R4 Wifi.

### Funkcje
- Tworzy otwarty punkt dostępowy WiFi o nazwie `ZaurScript_AP` (możliwość ustawienia hasła)
- Udostępnia pliki `.zs` (ZaurScript) zapisane w pamięci flash
- Kompatybilny tylko z ZaurParserem na UNO R4 Wifi
- Jeśli nie istnieje `main.zs`, tworzy domyślny plik

### Użytkowanie
1. Wgraj MicroPython na ESP8266.
2. Prześlij plik `zaurscript_ap_server.py` i pliki `.zs` na ESP8266.
3. Uruchom skrypt na ESP8266.
4. Połącz się urządzeniem ZaurParser z siecią WiFi `ZaurScript_AP`.
5. ZaurParser na UNO R4 Wifi może teraz pobierać pliki `.zs` z serwera AP ESP8266.
