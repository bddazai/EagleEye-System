# Components & Budget: Eagle Eye Budget Edition

This document details the hardware and software costs for a single Eagle Eye unit, optimized for a **₦10,000,000** cap.

## 1. Hardware Stack (Single Unit)

| Component | Specification | Estimated Cost (NGN) | Source/Alternative |
| :--- | :--- | :--- | :--- |
| **UAV Platform** | Refurbished DJI Matrice 210 RTK | ₦5,500,000 | Used Market (Lagos/Abuja) |
| **Primary Payload** | FLIR Lepton 3.5 + Breakout Board | ₦1,000,000 | Import/Specialist Tech Vendor |
| **Zoom Camera** | 30x Optical Zoom (Zenmuse Z30 Refurb) | ₦1,500,000 | Used Market |
| **Comms Module** | Huawei MS2372h + 4G MIMO Antennas | ₦350,000 | Local Electronics Vendor |
| **Edge Computing** | Jetson Nano (for AI Processing) | ₦250,000 | Local Electronics Vendor |
| **Ground Station** | Rugged 10" Android Tablet (Blackview) | ₦300,000 | Konga/Jumia |
| **Power Solution** | 4x TB55 Batteries (Refurb/Generic) | ₦600,000 | Specialist Battery Vendor |
| **Maintenance Kit** | Spare Props, Motors, Basic Tools | ₦300,000 | Local Sourcing |
| **TOTAL HARDWARE** | | **₦9,800,000** | |

## 2. Software Stack (Free & Open Source)

| Component | Software | Cost (NGN) | Purpose |
| :--- | :--- | :--- | :--- |
| **Flight Control** | DJI Pilot (Standard) | ₦0 | Basic operation. |
| **Object Detection** | OpenCV + TensorFlow Lite | ₦0 | Real-time human/vehicle ID. |
| **Telemetry** | QGroundControl (Customized) | ₦0 | Advanced mission planning. |
| **Alert Gateway** | Python Telegram Bot API | ₦0 | Secure instant notifications. |
| **TOTAL SOFTWARE** | | **₦0** | |

## 3. Local Sourcing & Implementation Notes
- **Lagos (Computer Village):** Primary source for LTE modems, Raspberry Pi/Jetson modules, and generic drone parts.
- **Abuja (Garki):** Best for sourcing used enterprise drone gear from security contractors.
- **Integration:** The FLIR Lepton is mounted on the M210 using a custom 3D-printed bracket (₦20,000 local printing) and fed into the Jetson Nano for processing.

## 4. Financial Summary
- **Target Budget:** ₦10,000,000
- **Actual Estimate:** **₦9,800,000**
- **Buffer:** ₦200,000 (for logistics and local assembly).

## 5. Decisions & Rationale
1. **Refurbished M210:** Selected over custom Pixhawk for better IP-rating and "out-of-the-box" stability required by law enforcement.
2. **FLIR Lepton 3.5:** High enough resolution for human detection at 500m while staying within the ₦1M price bracket.
3. **LTE Comms:** Using Huawei MS2372h (₦350k) instead of proprietary mesh (₦14M) to meet the ₦10M budget. Relies on local network coverage but is highly cost-effective.
