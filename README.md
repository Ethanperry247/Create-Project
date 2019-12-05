# Create_Project

**Title:** Thermal Node Network

**Author:** Ethan Perry

**Description:** Thermal Node Network is an attempt at making a smart fire detection and investigation system. The system utilizes wireless nodes connected to one master computer using Xbee 802.15.4 radios. If any node detects fire, it sends off a signal to the master node, which sounds an alarm, writes the event to a log file, and displays the location of the alarming node in a 3D visualization powered by openGL. Additionally, an robot may be controlled by the master node which can investiagte and discover any sources of fire near the desired area.

**Features:** Fire detection through various sensors (light, IR fire, temperature, gas, smoke, carbon monoxide, humidity), data logging, 3D visualization, alarms (light and sound), robot control, wireless node communication.

**Operation Instructions:** Raspberry pi nodes are required for the operation of this program. They may have any number of sensors, but they must have at least one sensor in order to fire off an alarm signal. Each raspberry pi must have an xbee 802.15.4 radio model S1 or higher. Additionally, a IRobot Create TM Robot must be connected to a node in order to use that functionality of the program. Pi_Main.py should be launched on any subsidiary nodes, and Main.py should be launched on the master node. Additionally, the visualizer must be launched on the master node in order to see the 3D visualization. 

**Notes:** This is not yet a fully functioning system, but na abstraction of a possibly larger system. The network can currently support a maximum of six nodes and one master. Though this could theoretically cover the entirety of one room, the dream of this project is to create a mesh network of thermal nodes spanning the entirety of buildings. Nonetheless, the thermal node network demonstrates the possibility of a technology such as that.
