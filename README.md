# Iterated Prisoner's Dilemma Project

## Overview
The Iterated Prisoner's Dilemma (IPD) is a classic problem in game theory that explores cooperation and competition between two players. This project aims to simulate the IPD, allowing users to implement various strategies and analyze their performance against each other across multiple iterations.

## Features
- **Multiple Strategies**: Implement various player strategies, including Tit for Tat, Always Cooperate, Always Defect, and others.
- **Simulation Environment**: A customizable framework for simulating games between different strategies over multiple rounds.
- **Data Analysis**: Tools for analyzing the results of games, including win rates, scores, and strategy effectiveness.
- **Visualization**: Graphical representations of results to better understand the dynamics of different strategies.

## Usage Instructions
1. **Clone the Repository**:  
   Use `git clone https://github.com/herio133/game-theory-slop.git` to clone the repository.

2. **Navigate to the Project Directory**:  
   `cd game-theory-slop`

3. **Run the Simulation**:  
   Execute the main script (e.g., `python ipd_simulation.py`) to start the game.

4. **Customize Strategies**:  
   Modify or implement new strategies in the `strategies.py` file.

5. **Analyze Results**:  
   After each run, results will be saved in the `results` directory for further analysis.

## Key Insights about Repeated Games and the Folk Theorem
- **Cooperation vs. Defection**: In a one-shot game, defection is the dominant strategy. However, when the game is played repeatedly, cooperation becomes a viable strategy.
- **Folk Theorem**: The Folk Theorem states that in an infinitely repeated game, a wide variety of outcomes can be sustained by cooperation, depending on the players' strategies and the shadow of the future (the discount factor). This result emphasizes the significance of future interactions in determining optimal behavior.

Understanding these concepts is crucial for analyzing strategic interactions in various fields, including economics, political science, and evolutionary biology.