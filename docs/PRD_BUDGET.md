# PRD: Eagle Eye Drone Surveillance (Budget Edition)

## 1. Executive Summary
The Eagle Eye Budget Edition is a cost-optimized, industrial-grade drone surveillance system designed for Nigerian Local Government Areas (LGAs). It aims to provide high-quality aerial security for under ₦10 million per unit, utilizing refurbished enterprise hardware and open-source software.

## 2. Problem Statement
Security budgets in many Nigerian LGAs are limited, yet the threat of banditry and kidnapping requires immediate, high-tech intervention. Standard enterprise drone packages (₦30M+) are unaffordable for widespread adoption.

## 3. Goals & Objectives
- **Goal:** Deliver a functional surveillance system within a ₦10M budget.
- **Objective 1:** Provide thermal imaging capability for night-time forest surveillance.
- **Objective 2:** Ensure 7km+ real-time video transmission range.
- **Objective 3:** Integrate with local law enforcement via standard LTE/4G networks.
- **Objective 4:** Establish a "Local Modular Maintenance" model to reduce downtime.

## 4. Target Audience
- LGA Security Councils.
- Nigeria Police Force (Divisional Offices).
- Local Vigilante Commanders.

## 5. System Architecture (Budget-Optimized)
### 5.1 Hardware
- **Platform:** Refurbished DJI Matrice 210 RTK (Dual Gimbal Support, IP43).
- **Primary Sensor:** FLIR Lepton 3.5 (Thermal) integrated via custom Raspberry Pi/Jetson carrier.
- **Secondary Sensor:** 30x Optical Zoom Camera (Low-light capable).
- **Connectivity:** Huawei MS2372h LTE Industrial Modem + High-gain MIMO Antennas.
- **Ground Station:** Ruggedized Android Tablet with custom open-source telemetry.

### 5.2 Software
- **OS:** Linux (Ground Station) / Android.
- **Vision:** OpenCV + TensorFlow Lite (on-edge person/vehicle detection).
- **Alerts:** Automated Telegram Bot for coordinate sharing with ground troops.

## 6. Functional Requirements
- **FR1:** Detect human heat signatures at 500m in total darkness.
- **FR2:** Stream 720p video to a remote command center via 4G.
- **FR3:** 30-minute minimum flight time per battery set.
- **FR4:** Secure local storage of all surveillance footage.

## 7. Success Criteria
1. Total hardware cost < ₦10 million per unit.
2. System survives IP43 dust/rain testing.
3. Successful real-time threat detection (human/vehicle) during night trials.
