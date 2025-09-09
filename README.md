
# 🎲 From Chaos to Randomness: Dice Simulation with the Hénon Map

This project explores how chaotic dynamics (Hénon map) can be used as a **pseudo-random number generator** to simulate dice rolls.

---

## 📂 Code Structure
- **main.py** → Hénon map generator + dice histogram.

---

## 🔑 Important Variables
- `a`, `b` → Hénon map parameters (default: 1.4, 0.3)  
- `x0`, `y0` → initial conditions  
- `N_throws` → number of dice rolls  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Adjust `a`, `b`, and initial conditions to see different chaotic sequences.  
3. Change `N_throws` to test statistical convergence.  
4. Run:
   ```bash
   python main.py


---

## 🧠 Physical/Statistical Intuition

* The Hénon map generates deterministic chaos.
* Mapping chaotic numbers to dice faces creates a non-uniform but pseudo-random distribution.
* RMS deviations of probabilities shrink with more throws:

  $$
  \sigma \sim \frac{1}{\sqrt{N}}
  $$

---

## 🧮 Numerical Models

* **Chaotic map iteration** (Hénon map)
* **Monte Carlo dice mapping** from chaotic sequences
* **Fluctuation–Dissipation scaling** analysis


