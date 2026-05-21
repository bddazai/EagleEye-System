# Components & Cost Estimation: Eagle Eye Surveillance Initiative

This document outlines the hardware, software, and operational costs for a single "Eagle Eye" unit.

## 1. Hardware Stack (Per Unit)

| Component | Specification | Estimated Cost (USD) | Estimated Cost (NGN) | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **UAV Platform** | DJI Matrice 350 RTK | $15,000 | ₦21,750,000 | Core flight platform, IP55 rated. |
| **Primary Payload** | Zenmuse H20T | $10,000 | ₦14,500,000 | Thermal, 23x Zoom, Laser Rangefinder. |
| **Secondary Payload** | Zenmuse H20N | $4,000 | ₦5,800,000 | Night Vision + Starlight sensor. |
| **Backhaul Comms** | Starlink High-Performance Kit | $2,500 | ₦3,625,000 | High-speed data in remote areas. |
| **Tactical Comms** | Silvus StreamCaster 4200 (2x) | $10,000 | ₦14,500,000 | Secure local mesh for ground units. |
| **Power Solution** | Mobile Solar Charging Hub | $3,500 | ₦5,075,000 | Independent power for remote base. |
| **Spares & Accs** | TB65 Batteries (x8), Props, RC | $4,000 | ₦5,800,000 | Operational continuity. |
| **TOTAL HARDWARE** | | **$49,000** | **₦71,050,000** | |

*Note: Exchange rate estimated at 1 USD = ₦1,450.*

## 2. Software & Licensing

| Service | Plan | Annual Cost (USD) | Purpose |
| :--- | :--- | :--- | :--- |
| **DJI FlightHub 2** | Professional | $1,500 | Fleet management & cloud live-streaming. |
| **Starlink Priority** | 1TB Priority | $1,200 | High-bandwidth dedicated uplink. |
| **Alert Gateway** | Twilio/WhatsApp API | $300 | Automated community alert distribution. |
| **TOTAL SOFTWARE** | | **$3,000** | |

## 3. Local Sourcing Suggestions (Nigeria)

To ensure sustainability and ease of maintenance, the following local partners are recommended:

1. **Hardware Procurement:**
   - **Geoinfotech (Lagos/Abuja):** Authorized DJI Enterprise dealer for warranty support.
   - **ARCO Worldwide Services:** Specialized in high-security UAV deployments.
2. **Solar Infrastructure:**
   - **Lumos Nigeria / Zola Electric:** For ruggedized mobile solar battery solutions.
3. **Connectivity:**
   - **Starlink.com:** Direct purchase for best pricing.
4. **Maintenance:**
   - Establish a local "Maintenance Hub" within the LGA Secretariat, trained by the authorized dealer.

## 4. Total Project Cost (Year 1)

- **Initial Setup (CapEx):** $49,000
- **Operational Software (OpEx):** $3,000
- **Training & Integration (Consultancy):** $3,000
- **GRAND TOTAL:** **$55,000** (First Unit)
- **SCALE-UP COST:** **$50,000** (Subsequent units)

## 5. Decision Log
- **M350 RTK vs M30T:** Selected M350 for its modularity and ability to carry heavier/multiple payloads (H20T + H20N).
- **Starlink vs GSM:** Selected Starlink due to the high failure rate and "jamming" potential of GSM networks in bandit-prone forest areas.
- **Mesh Selection:** Silvus Technologies chosen for their proven performance in dense vegetation/NLOS (Non-Line-of-Sight) conditions.
