ESP Bluetooth Connection and Joystick Integration

This project demonstrates using ROS 2 services with an ESP device connected via Bluetooth. The ESP is paired and connected through the terminal, bound to a serial port, and joystick commands are read using joy_node.

The workflow is as follows:

Connect ESP Bluetooth
The ESP device is paired, trusted, and connected via bluetoothctl using its MAC address.

Bind Bluetooth for Serial Communication
Once connected, the ESP is bound to /dev/rfcomm0 for serial communication using rfcomm.

Read Joystick Commands with ROS 2
The joy_node from the ROS 2 joy package reads input from the joystick, allowing interaction with the ESP via ROS services.

This setup allows seamless demonstration of ROS 2 service features, combining wireless communication with real-time joystick input.
