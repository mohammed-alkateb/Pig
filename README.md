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



## ⚙️  Running Tests

To run tests, run the following command

```bash
  <File> pytest
```
Example of running test
![App Screenshot](https://user-images.githubusercontent.com/92877244/222927770-de694b2e-cea9-4561-84e3-bf2557fa3c3a.png)




## License

[MIT](https://choosealicense.com/licenses/mit/)

This project is licensed under the terms of the MIT license.

