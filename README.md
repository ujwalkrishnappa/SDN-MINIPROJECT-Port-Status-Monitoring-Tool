# SDN Port Status Monitoring Tool using Mininet & Ryu

## Project Overview

This project monitors switch port status in a Software Defined Network (SDN) using Mininet and the Ryu controller.
It detects port UP/DOWN events, generates alerts, and logs all changes with timestamps.

---

## Problem Statement

In traditional networks, detecting link or port failures is difficult and slow.
This project solves that problem by providing real-time monitoring of port status using SDN.

---

## Objective

* Detect port status changes (UP/DOWN)
* Generate alerts for failures
* Log events with timestamps
* Analyze network impact

---

## Tools Used

* Mininet
* Ryu Controller
* OpenFlow Protocol (v1.3)
* Python

---

## Setup Steps

1. Install Mininet

2. Install Ryu:

   ```bash
   pip3 install ryu
   ```

3. Run the controller:

   ```bash
   ryu-manager port_monitor.py
   ```

4. Run Mininet:

   ```bash
   sudo mn --topo=single,2 --controller=remote --switch ovsk,protocols=OpenFlow13
   ```

---

## Execution Steps

* Check connectivity:

  ```bash
  pingall
  ```

* Bring port down:

  ```bash
  link s1 h1 down
  ```

* Bring port up:

  ```bash
  link s1 h1 up
  ```

---

## Expected Output

* Controller detects port changes
* Alerts printed when port goes DOWN
* Logs saved in `port_log.txt`
* Network failure visible during ping

---

## Results

* Port failures successfully detected
* Real-time alerts generated
* Logs stored with timestamps
* Network behavior observed using ping

---

## Conclusion

This project demonstrates how SDN can be used for efficient real-time network monitoring and failure detection using a centralized controller.

---

## References

* Mininet Documentation
* Ryu SDN Framework
