from three_reel_slot import SlotMachine
import csv

reel_strip = ["Cherry"] * 14 + ["Lemon"] * 9 + ["Bell"] * 4 + ["Bar"] * 2 + ["Seven"]
payout_table = {"Cherry": 2, "Lemon": 4, "Bell": 10, "Bar": 30, "Seven": 100}

cost_per_spin = 0.3546 # for RTP to be 98%
machine = SlotMachine(reel_strip, payout_table, cost_per_spin)

spin_cnt = int(input("Number of spins: "))

total_payout = 0
win_count = 0
with open("convergence.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Spin", "Cumulative RTP"])

    for i in range(spin_cnt):
        symbols, payout =  machine.spin()
        total_payout += payout
        if payout > 0:
            win_count += 1
            
        if (i + 1) % 1000 == 0:
            cumulative_rtp_pct = (total_payout / (i + 1)) / cost_per_spin
            writer.writerow([i+1, cumulative_rtp_pct])
            



print(f"Hit frequency: {win_count / spin_cnt:.4f}")
print(f"Expected: ~0.1316")