# EagleEye Surveillance System 🦅
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, scalable, and cost-effective drone surveillance system designed for Nigerian Local Governments to combat banditry and insecurity.

## 🌟 Overview
EagleEye provides a dual-tiered architecture (High-End & Budget) to ensure that every Local Government Area (LGA) in Nigeria can deploy advanced aerial surveillance regardless of budgetary constraints. The system integrates UAVs, thermal imaging, and AI-driven edge detection to provide real-time intelligence to law enforcement and community vigilantes.

## 🏗️ System Tiers
| Feature | [High-End Unit](./hardware/COMPONENTS_HIGH_END.md) | [Budget Unit](./hardware/COMPONENTS_BUDGET.md) |
| :--- | :--- | :--- |
| **Drone** | DJI Matrice 350 RTK | Refurbished DJI Matrice 210 RTK |
| **Sensors** | Zenmuse H20T (Thermal/Zoom/Laser) | FLIR Lepton 3.5 + 30x Zoom |
| **Comms** | Starlink + Silvus Mesh | 4G LTE (Huawei/MIMO) |
| **Target Cost** | ~$50,000 (₦72.5M) | < ₦10,000,000 |
| **Best For** | Strategic forest/border patrol | Community perimeter security |

## 📁 Repository Structure
```text
EagleEye-System/
├── docs/               # Strategy, PRDs, and Case Studies
├── hardware/           # Bill of Materials and Assembly Guides
├── software/           # Edge AI and Alerting scripts
├── media/              # Screenshots and demo references
└── LICENSE             # MIT License
```

## 🚀 Getting Started
### Prerequisites
- DJI Enterprise UAV (M350/M300/M210).
- Linux-based Ground Station or Android Tablet.
- For AI features: NVIDIA Jetson Nano or Raspberry Pi 4.

### Deployment Steps
1. **Hardware Assembly:** Follow the [Budget Assembly Guide](./hardware/ASSEMBLY_GUIDE_BUDGET.md) or [High-End Guide](./docs/OPERATIONAL_GUIDE_HIGH_END.md).
2. **Software Setup:** 
   ```bash
   cd software/
   pip install -r requirements.txt
   python alert_bot.py --token YOUR_BOT_TOKEN
   ```
3. **Field Operation:** Refer to the [Operational Protocols](./docs/OPERATIONAL_PROTOCOL.md).

## 📊 Proof of Effectiveness
Documented cases in Kaduna and Zamfara show a **40-60% reduction in response time** and a **significant decrease in kidnapping incidents** following the deployment of similar persistent aerial surveillance. See [Case Studies](./docs/CASE_STUDIES.md) for more details.

## 🤝 Contributing
We welcome contributions from drone pilots, software engineers, and security experts. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Empowering Nigerian communities through technology.*
