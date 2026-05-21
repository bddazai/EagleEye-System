# Assembly & Operational Guide: Eagle Eye Budget Edition

This guide details how to assemble, deploy, and operate the budget-optimized Eagle Eye system.

## 1. Physical Assembly

### Step 1: Drone Preparation
- Inspect the refurbished DJI Matrice 210 for structural integrity.
- Update firmware to the latest stable version using DJI Assistant 2.
- Mount the 30x Zoom Camera on the primary gimbal port.

### Step 2: Thermal Sensor Integration
- Mount the **FLIR Lepton 3.5** to the **Jetson Nano** using the breakout board.
- Secure the Jetson Nano to the top mounting plate of the M210.
- Connect the Jetson Nano to a 5V/3A power source from the M210's expansion port.
- Link the Jetson's video output to the M210's FPV camera feed or use the LTE module to stream directly to the ground station.

### Step 3: Communication Setup
- Insert a high-speed 4G SIM card (MTN or Airtel) into the **Huawei MS2372h** modem.
- Attach the MIMO high-gain antennas to the modem.
- Configure the modem as a transparent bridge or VPN endpoint for secure data transmission.

## 2. Software Configuration

### Step 1: Edge Intelligence
- Flash the Jetson Nano with the Eagle Eye OS image (Ubuntu-based).
- Run the `install_cv.sh` script to set up OpenCV and TensorFlow Lite.
- Load the pre-trained `person_vehicle_detector.tflite` model.

### Step 2: Ground Station Setup
- Install the custom **QGroundControl** APK on the rugged tablet.
- Configure the Telegram Bot API key in the `alert_config.json` file.
- Verify that the 4G signal strength is >-90 dBm for reliable streaming.

## 3. Operational Protocols

### Pre-Flight Checklist
1. Verify battery voltage (minimum 25.2V per pair).
2. Check propeller condition and motor rotation.
3. Confirm 4G signal and VPN tunnel status.
4. Perform a quick thermal sensor calibration.

### In-Flight Maneuvers
- **Forest Sweep:** Fly at 100m AGL, using the thermal sensor to look for anomalies in the canopy.
- **Threat Verification:** Drop to 50m AGL and engage the 30x zoom camera to identify targets.
- **Coordinate Sharing:** Use the "Send Alert" button on the tablet to push GPS coordinates to the law enforcement Telegram group.

## 4. Maintenance (Local Modular)
- **Propellers:** Replace every 50 flight hours or if any nicks are found.
- **Motors:** Apply dry lubricant every 100 hours.
- **Lenses:** Clean with isopropyl alcohol after every flight in dusty conditions.
- **Batteries:** Store at 50% charge if not flying for more than 48 hours.

## 5. Security Mitigation
- **Jamming:** If the signal is lost, the drone is programmed to "Return to Home" (RTH) automatically using GPS/GLONASS.
- **Vulnerability:** Use a WireGuard VPN for all 4G traffic to prevent eavesdropping on the video feed.
