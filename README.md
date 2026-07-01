# Slot Machine Mathematical Analysis

A complete game mathematics project demonstrating the full workflow: theoretical derivation, Monte Carlo simulation, 
and statistical validation.



---

## Game Design

Three-reel slot machine with five weighted symbols and a 98% RTP target.

| Symbol | Weight | Probability | Payout (3-of-a-kind) |
|--------|--------|-------------|----------------------|
| Cherry | 14/30  | 46.67%      | 2                    |
| Lemon  | 9/30   | 30.00%      | 4                    |
| Bell   | 4/30   | 13.33%      | 10                   |
| Bar    | 2/30   | 6.67%       | 30                   |
| Seven  | 1/30   | 3.33%       | 100                  |

**Win condition:** three-of-a-kind only. Cost per spin: 0.3546 credits (derived from 98% RTP target).

---

## Theoretical Analysis

All metrics derived analytically before simulation.

**Win probability per symbol:**

$$P(\text{3-of-a-kind}_s) = \left(\frac{w_s}{30}\right)^3$$

**RTP:**

$$\text{RTP} = \frac{E[X]}{c} = \frac{\sum_s P_s \times \text{payout}_s}{c} = \frac{0.3476}{0.3546} = 98\%$$

**Hit frequency:**

$$P(\text{win}) = \sum_s P_s \approx 13.16\%$$

**Variance:**

$$\text{Var}(X) = E[X^2] - (E[X])^2 = 1.7119 - 0.1208 = 1.5911$$

$$\sigma = \sqrt{\text{Var}(X)} \approx 1.2614$$

---

## Simulation Results

Validated at 10,000,000 spins using a Python Monte Carlo engine.

| Metric         | Theoretical | Simulated  | Difference |
|----------------|-------------|------------|------------|
| RTP            | 98.00%      | 97.95%     | -0.05%     |
| Hit Frequency  | 13.16%      | 13.12%     | -0.04%     |
| Variance       | 1.5911      | 1.5925     | +0.0014    |
| Std Deviation  | 1.2614      | 1.2620     | +0.0006    |

---

## Charts

### Symbol Frequency: Simulated vs Theoretical
![Symbol Frequency](charts/chart1_symbol_frequency.png)

### Payout Distribution
![Payout Distribution](charts/chart2_payout_distribution.png)

### RTP Convergence
![RTP Convergence](charts/chart3_rtp_convergence.png)

---

## Convergence Analysis

Different metrics converge at different rates due to the heavy-tailed nature 
of the payout distribution. Hit frequency converges quickly (binary outcome, 
relatively high probability). RTP and variance converge slowly because rare 
high-payout symbols (Seven: 0.0037% probability, 100 credit payout) dominate 
higher-order moment calculations but appear infrequently at small sample sizes.

The Seven symbol alone contributes 21.6% of E[X²] despite its near-zero probability — 
requiring millions of spins before variance estimates stabilize.

---

## Project Structure

slot-machine-math/

├── src/

│   ├── three_reel_slot.py    # SlotMachine class, simulate/play modes

│   └── convergence.py        # RTP convergence tracker

├── data/

│   ├── three_reel_slot_simulation.csv

│   └── convergence.csv

├── charts/

│   ├── chart1_symbol_frequency.png

│   ├── chart2_payout_distribution.png

│   └── chart3_rtp_convergence.png

└── report/

└── slot_machine_math_report.pdf

---

## Usage

```bash
python src/three_reel_slot.py
# Choose mode: play or simulate
```

```bash
python src/convergence.py
# Generates convergence.csv with cumulative RTP at 1000-spin intervals
```

---

## Requirements

Python 3.x, standard library only (random, csv, math). No external dependencies.

---

## Author

**Pavle Pavlović**  
Computer Technician
Electrical and Computer Engineering Student (RF/Microwave Engineering)
University of Belgrade, School of Electrical Engineering
