# Installing and Running the TCG Project

To install and run the TCG project, you can follow these steps:

## Requirements

Make sure that your system meets the following requirements:

- Python 3.6 or higher
- pip 20.0.2 or higher

## Installation

1. Clone the TCG project repository:

```
$ git clone https://github.com/WyldKnyght/tcg-project.git
```

2. Navigate to the cloned repository directory:

```
$ cd tcg-project
```

3. Install the required Python packages using pip:

```
$ pip install -r requirements.txt
```

## Running the TCG Project

1. Open a terminal and navigate to the directory containing the `predict.py` script using the `cd` command.

2. Type the following command to run the script:

```
$ python predict.py
```

This will prompt you to provide the file paths for two Pokemon Trading Card Game deck files in JSON format. The script will then predict the outcome of a match between the two decks and output the predicted probabilities for each possible outcome (win or loss). The results of the prediction will be outputted to the terminal.

If you encounter any issues while installing or running the TCG project, please refer to the troubleshooting section in the `user_guide.md` file.
