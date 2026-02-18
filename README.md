connect the esp bluetooth from terminal
cmd-
bluetoothctl 
pair MAC
trust MAC
connect MAC


after that bind the bluetooth for serial connection 
cmd-
sudo rfcomm bind /dev/rfcomm0 MAC 1

Also need joy_node for reading the joy stick commands
run the joy_node
ros2 run joy joy_node

