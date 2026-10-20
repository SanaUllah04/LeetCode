# Python Problem-Solving Notes

A growing collection of Python solutions, coding exercises, and small experiments. The repository is organized by difficulty, with a separate folder for miscellaneous projects.

> **A work in progress:** files are practice solutions, not a package or a fully tested reference library. Some solutions are written for the LeetCode `Solution` class interface; others run as standalone scripts.

## At a glance

| Collection | What's inside |
| --- | --- |
| [`Easy/`](Easy/) | Foundational algorithm exercises |
| [`Medium/`](Medium/) | Array and scheduling problems |
| [`Hard/`](Hard/) | More involved algorithm challenges |
| [`Random/`](Random/) | Miscellaneous practice, including a playable trivia game |

## Solutions and exercises

### Easy

| Exercise | File |
| --- | --- |
| Find the second-largest value | [`2ndlargest.py`](Easy/2ndlargest.py) |
| Climbing Stairs (Fibonacci approach) | [`Climbing_Stairs_(Fibonacci Series).py`](<Easy/Climbing_Stairs_(Fibonacci Series).py>) |
| Generate Pascal's Triangle | [`Pascal's Triangle.py`](<Easy/Pascal's Triangle.py>) |
| Two Sum | [`Sum_Of_Two.py`](Easy/Sum_Of_Two.py) |
| Alternating arithmetic calculation | [`alternating_calc.py`](Easy/alternating_calc.py) |
| Count adjacent consecutive values | [`consecutive.py`](Easy/consecutive.py) |
| Identify frequent users in a request list | [`spammyUsers.py`](Easy/spammyUsers.py) |

### Medium

| Exercise | File |
| --- | --- |
| Minimum workers needed for overlapping shifts | [`EmployeeShift.py`](Medium/EmployeeShift.py) |
| Product of array except self | [`productList.py`](Medium/productList.py) |
| Meeting-room scheduling | [`schulde.py`](Medium/schulde.py) |

### Hard

| Exercise | File |
| --- | --- |
| Brick placement / stacking simulation | [`Putting away the bricks.py`](<Hard/Putting away the bricks.py>) |

## Miscellaneous project: Trivia Madness

[`Random/Trivia Game/Trivia_Game.py`](<Random/Trivia Game/Trivia_Game.py>) is a terminal trivia game with question loading, question entry, score tracking, and a leaderboard.

Run it from its own folder so the game can find its data files:

```console
cd "Random/Trivia Game"
python Trivia_Game.py
```

Questions are read from [`quest_load.txt`](<Random/Trivia Game/quest_load.txt>) in `question|answer|points` format. The game reads and writes the leaderboard in [`leaders.txt`](<Random/Trivia Game/leaders.txt>).

## Running a solution

Python 3 is required. Run a standalone exercise from the repository root, for example:

```console
python Easy/alternating_calc.py
```

Some files define a `Solution` class and expect inputs to be supplied by an online judge or your own test harness. A few exercise scripts include sample data and print statements; inspect the file before running it.

## Repository layout

```text
.
├── Easy/                 # Foundational exercises
├── Medium/               # Intermediate exercises
├── Hard/                 # Advanced exercises
└── Random/
    └── Trivia Game/      # Terminal game and its data files
```
