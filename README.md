# 🀄 Domino-Strategist: Bayesian Logic Engine
A Python-based decision-support tool for the game of Dominoes. This engine uses deductive logic and weighted heuristics to track the board state, predict opponent hands, and suggest the mathematically optimal play.
## 🚀 Overview
Unlike basic domino simulators, this engine implements probabilistic tracking. It monitors every "pass" in the game to build a profile of what numbers each player is unable to hold, allowing it to "trap" opponents and support partners with high precision.

## 🧠 Strategic Heuristics
The engine evaluates the "Best Move" by calculating a score for every legal tile in your hand using the following formula:\
<p align="center"><i>Score</i> = <i>S<sub>partner</sub></i> + <i>B<sub>opponent</sub></i> + <i>C<sub>control</sub></i></p>
**Partner Support (_S_):** Analyzes the teammate's history. If a move creates an end that the partner is known to be missing, the score is penalized.\
**Opponent Blocking (_B_):** Boosts the score if the resulting board end matches a number an opponent has previously passed on.\
**Maintaining Control (_C_):** Uses frequency counting to ensure you retain tiles that allow you to dictate the flow of the game.

## 🛠 Features
* Dynamic Hand Tracking: Monitors the remaining 28 tiles in the deck (the "boneyard").
* **Player Profiling:** Automatically updates a cannot_have database for all 4 players based on game events.
* **Double-Six Compatibility:** Designed for the standard 28-tile set.
* **Weighted Decision Matrix:** Scores tiles based on multiple defensive and offensive factors.
* 
## 📖 How to Use
1. Initialization:
Input your 7 starting tiles when prompted. The engine will remove these from the left (boneyard) set.
2. The Game Loop
The engine operates on three main event types:
* Turn 0 (Your Move): Input the current board ends. The AI will output the Best Domino to play.
* Turn 1 (Record Play): Input tiles played by others to keep the tracker accurate.
* Turn 2 (Record Pass): If a player passes, input the current ends. The AI now knows that player has *0* of those numbers.
* Turn 3 (Exit the game): If you want to exit the game loop and end the game.

## 💻 Code Structure
| component | Responsibility |
| --- | --- |
| `create_domino_set()` | Generates the initial 28-tile Cartesian product.|
| `cannot_have` | A dictionary-based truth table for player constraints.|
| `evaluate_maintaining_control()` | Uses `collections.Counter` to calculate hand density.|
| `calculate_the_best_tile()` | The core decision engine using weighted sums.|

## 📈 Future Roadmap
* [ ] GUI Interface: Transition from CLI to a visual board representation.
* [ ] MCTS Integration: Implement Monte Carlo Tree Search for deeper move look-ahead.
* [ ] Automated Board State: Auto-detect "ends" based on the sequence of tiles played.

## 🤝 Contributing
Contributions are welcome! If you have a heuristic that improves the win rate, feel free to fork and submit a PR.
create_domino_set(): 
