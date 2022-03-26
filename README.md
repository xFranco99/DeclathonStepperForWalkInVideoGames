# DeclathonStepperForWalkInVideoGames
Very small project for walking in videogames using Arduino and Python whith an old declathon stepper

Python libraries used for this project:
- serial
- time
- pynput
- directkeys

<b><h2>How it Work</h2></b> <br> <br>
The step used for this project is an old Declathon step like this: <br>
![step-resized](https://user-images.githubusercontent.com/45762539/160235707-d8272731-dc0e-40bf-a364-024076ccfac3.jpg) <br>
This step has a magnet sensor used for the step count <br>
![step_sensor_smaller](https://user-images.githubusercontent.com/45762539/160235785-62a0b40e-0dd1-44f5-bff0-0db4d959e644.jpg) <br>
and inside the metal structure there is a magnet that change position every step: <br>
![image](https://user-images.githubusercontent.com/45762539/160235930-62c7f198-938e-4096-8906-251a4a4316ef.png) <br>

Arduino get every state changing and write it on serial, then a python script get the serial values and press W every time the sensor change state.

Advertising: use this project for VR is not recommended, it causes motion sickness and loss of balance

Demonstration:
https://vm.tiktok.com/ZMLuqM4xu/
