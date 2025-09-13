# River Riddle — Safe Crossing Sequence

Objects: Farmer (F), Wolf (W), Goat (G), Cabbage (C)
Boat carries farmer + at most one item per trip.

Safe sequence of crossings (Farmer starts on the left bank with all items):
1. F takes G to the right bank.  (Left: W, C | Right: F, G)
2. F returns alone to the left bank.  (Left: F, W, C | Right: G)
3. F takes W to the right bank.  (Left: C | Right: F, W, G)
4. F brings G back to the left bank.  (Left: F, G, C | Right: W)
5. F takes C to the right bank.  (Left: G | Right: F, W, C)
6. F returns alone to the left bank.  (Left: F, G | Right: W, C)
7. F takes G to the right bank.  (Left: -- | Right: F, W, G, C)

All items are now safely on the right bank.

Notes:
- At no point are W and G left alone together without F.
- At no point are G and C left alone together without F.
- This is the classic minimal solution (7 boat trips total).