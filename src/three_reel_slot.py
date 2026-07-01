import random
import csv
import math

class SlotMachine:
    def __init__(self, reel_strip, payout_table, cost_per_spin):
        self.reel_strip = reel_strip
        self.payout_table = payout_table
        self.cost_per_spin = cost_per_spin

    def spin(self):
        reel1 = random.choice(self.reel_strip)
        reel2 = random.choice(self.reel_strip)
        reel3 = random.choice(self.reel_strip)

        if reel1 == reel2 and reel1 == reel3:
            return (f"{reel1}-{reel2}-{reel3}", self.payout_table[reel1]) 
        else:
            return (f"{reel1}-{reel2}-{reel3}", 0)
        
    def run_simulation(self, n_spins):
        total_payout = 0
        total_payout_sq = 0
        win_count = 0

        with open("three_reel_slot_simulation.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Spin", "Symbols", "Reel1", "Payout", "Win"])

            for i in range(n_spins):

                symbols, payout = self.spin()
                total_payout += payout
                total_payout_sq += payout ** 2
                reel1 = symbols.split("-")[0]

                if payout > 0:
                    win_count += 1

                writer.writerow([i+1, symbols, reel1, payout, 1 if payout > 0 else 0])

        return{
            "rtp_pct": total_payout / (n_spins * self.cost_per_spin),
            "hit_frequency": win_count / n_spins,
            "variance": total_payout_sq / n_spins - (total_payout / n_spins) ** 2,
            "std_dev": math.sqrt(total_payout_sq / n_spins - (total_payout / n_spins) ** 2)
        }
if __name__ == "__main__":

    reel_strip = ["Cherry"] * 14 + ["Lemon"] * 9 + ["Bell"] * 4 + ["Bar"] * 2 + ["Seven"]
    payout_table = {"Cherry": 2, "Lemon": 4, "Bell": 10, "Bar": 30, "Seven": 100}
    cost_per_spin = 0.3546 # for RTP to be 98%

    machine = SlotMachine(reel_strip, payout_table, cost_per_spin)

    mode = input("Choose mode (play/simulate): ").strip().lower()

    if mode == "simulate":
        spin_cnt = int(input("Number of spins: "))

        results = machine.run_simulation(spin_cnt)

        print(f"RTP: {results['rtp_pct']*100:.2f}%")
        print(f"Hit Frequency: {results['hit_frequency']*100:.2f}%")
        print(f"Variance: {results['variance']:.4f}")
        print(f"Std Dev: {results['std_dev']:.4f}")

    elif mode == "play":

        balance = float(input("Enter starting balance: "))
        while balance >= cost_per_spin:
            input("Press Enter to spin...\n")
            symbols, payout = machine.spin()
            balance -= cost_per_spin
            balance += payout
            
            print(f"{{{symbols.replace('-', '}-{')}}}")

            net = payout - cost_per_spin
            if payout > 0:
                print(f"WIN! You won {payout} credits! | Net: {net:+.2f}")
            else:
                print(f"No win. Try again! | Net: {net:+.2f}")

            print(f"Current balance: {balance:.2f}\n")

        
        print("Out of funds.\n")
    else:
        print("Invalid mode. Choose 'play' or 'simulate'.")
    