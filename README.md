# 🎲 Pig (dice game)
A simple dice game with two players. Each player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold". The player who first scores 100 or more points wins.


## 👨‍🎓 Authors
- [@shuaybw](https://www.github.com/shuaybw)
- [@mohammed-alkateb](https://www.github.com/mohammed-alkateb)


## ⚖️ Game rules

Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

- If the player rolls a 1, they score nothing and it becomes the next player's turn.
- If the player rolls any other number, it is added to their turn total and the player's turn continues.
- If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
  The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-6, after which she chooses to hold, and adds her turn total of 23 points to her score.


## ⚙️ Setup 

Clone the project using the web URL/HTTPS alternative

```bash
  git clone https://github.com/mohammed-alkateb/Pig.git
```

Clone the project using SSH alterative
```bash
  git clone git@github.com:mohammed-alkateb/Pig.git
```
Go to the game directory
```bash
  cd game.py
```
Install required dependencies
```bash
  pip instal <module name>
```
Run game
```bash
  Green run button
```



## ⚙️  Running Tests

To run tests first install pytest

```bash
  pip install -U pytest
```
To test code do the following
```bash
  pytest <file>
```
test run example
![App Screenshot](https://user-images.githubusercontent.com/92877244/222927770-de694b2e-cea9-4561-84e3-bf2557fa3c3a.png)




## 💾 License

[MIT](https://choosealicense.com/licenses/mit/)

This project is licensed under the terms of the MIT license.

## UMl
Graphviz
pyreverse


## 🗎 Regenerate Documentation

To install the package
```bash
  1. pip install sphinx
```
Run the package
```bash
  2. sphinx-quickstart
```
Regenerate a document file in HTML format
```bash
  3. make html
```


## 🎮 Gane Intelligence

We chose to implement two levels of automated enemy intelligence. The easy level is based on randomizing a number between 0 (Roll a die) and 1 (Hold). The hard level, on the other hand, uses the NumPy and Scikit-learn libraries. NumPy is used to load data from a file and return it as NumPy arrays. Scikit-learn is used to create a machine learning model for predicting the next dice roll value. In summary, in the hard level, the computer can predict the next dice roll value and make a decision based on whether to roll the dice or hold.
