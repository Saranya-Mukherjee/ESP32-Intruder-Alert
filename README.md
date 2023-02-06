# ESP32-Intruder-Alert

This project takes you through the steps on how to create an intruder alert system based on ESP32.

BOM:
1. ESP32 CAM with OV2640 camera module.
2. FTDI programmer or Arduino board. [This tutorial uses an arduino board to upload code for simplicity]

STEP 1: 
Prepare Arduino as an FTDI code uploader.
To do the same, make the following circuit.

![image](https://user-images.githubusercontent.com/71862329/216975315-b719a798-13b3-46eb-9b5e-14a9a778abb7.png)

Now go into arduino IDE:
1. Add this URL to preferences: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
2. Go to boards and install: "ESP32"
3. Open up 'tools' and select the following settings: ![image](https://user-images.githubusercontent.com/71862329/216975614-420b5182-d806-45a8-a4d7-17d20b5640be.png)
4. After plugging in your Arduino, the corrosponding COM port will show up; select that port.

STEP 2:
Upload the code:
1. You will need arduino IDE 1.8.19 or higher or some of the libraries wont compile properly.
2. Open up the Arduino Code provided in the Git Repo; Put your WIFI credentials into the code before uploading.
3. Click on upload on the arduino IDE. When red coloured dots start to appear on the screen, proceed to the next step.
4. Short the GPIO 0 and the GND pins on the ESP32 board for 1-2 sec (you may have to check how long your board needs to be shorted) to put the board into boot-loader mode. When the code starts to upload, release the short.
5. After the code has completely uploaded, press the reset button on the ESP32 board.

Step 3:
Get the python code running:
1. Download the python code from th git repo [included in folder: IntruderAlert]. Also download the provided HaarCascades.
2. Open up the code in your preferred editor.
3. Install "Open CV", "Numpy", "Matplotlib" and "Pandas" for python.
4. Get the IP of the WebServer created by the ESP32 board and insert it into the code.
5. Run to code.

Step 4:
How to get the IP address of the ESP32 board:
1. Attach the Arduino-ESP32 system as told before to the computer.
2. Open Serial Monitor in Arduino IDE.
3. Press "reset" on the ESP32 board and wait for it to connect to the wifi network.
4. The ESP32 board will print its IP address to the serial monitor once it has connected to the network.

Step 5:
Running the code:
1. Red squares means that it detects motion.
2. Green squares means that it detects faces.
3. Yellow squares means that it detects people.
4. If any suspisious behaviour is detected, then the word "DETECTED" is written on top of the preview window.
5. Press 'k' to reset the system; Press 'q' to close all systems.

The End.
