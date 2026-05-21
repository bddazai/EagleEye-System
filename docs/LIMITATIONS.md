# Known Limitations & Risk Mitigation: Eagle Eye Budget Edition

This document outlines the operational constraints of the budget-optimized system and provides strategies for mitigation.

## 1. Environmental Constraints
- **Weather (Rain/Dust):** The M210 is IP43 rated, meaning it can handle light rain and dust but not heavy downpours or sandstorms.
    - *Mitigation:* Operators must ground the aircraft during severe weather. Use the high-gain 30x zoom from a distance to minimize exposure to dust clouds.
- **Wind:** Flight stability is compromised in winds exceeding 12 m/s.
    - *Mitigation:* Real-time wind speed monitoring on the ground station; automated RTH if wind limits are exceeded.

## 2. Technical Limitations
- **Communication Reliability:** Unlike proprietary mesh systems, 4G LTE relies on local carrier (MTN/Airtel) uptime.
    - *Mitigation:* Use dual-SIM modems for carrier redundancy. Implement local recording (SD card) for later retrieval if the stream fails.
- **Sensor Resolution:** The FLIR Lepton 3.5 has a lower resolution than high-end thermal sensors (H20T).
    - *Mitigation:* Fly at lower altitudes (70m-100m) for better thermal clarity and use AI-assisted edge detection to highlight anomalies.

## 3. Security Vulnerabilities
- **Signal Jamming:** 4G signals can be jammed by sophisticated bandit groups using basic GPS/GSM jammers.
    - *Mitigation:* The drone is configured with "RTH on Signal Loss" using encrypted GPS/GLONASS. Implement frequency-hopping where possible with custom radio links if the budget allows in the future.
- **Data Privacy:** 4G data can be intercepted if not secured.
    - *Mitigation:* All telemetry and video traffic is tunneled through an AES-256 encrypted WireGuard VPN.

## 4. Maintenance Risks
- **Refurbished Hardware:** Used components have a higher risk of failure than new ones.
    - *Mitigation:* Implement a rigorous "50-Hour Full Audit" as detailed in the `ASSEMBLY_GUIDE.md`. Maintain a local stock of critical spares (motors, ESCs).

## 5. Regulatory Risks
- **NCAA Compliance:** Operating enterprise drones without proper licensing can lead to impoundment.
    - *Mitigation:* The LGA must secure an RPAS Operator's Certificate (ROC) and coordinate all flights with the nearest military/civilian air traffic control.
