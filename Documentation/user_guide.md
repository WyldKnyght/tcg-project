# User Guide

## Overview

- Introduction
- Main features
- Getting started

## Installation

- System requirements
- Installing dependencies
- Downloading and installing the model

## Usage

- Predicting match outcomes
- Customizing decks
- Training the model

## Troubleshooting

- Common issues and solutions

## Conclusion

- Additional resources
- License


## Introduction

The TCG project is a machine learning model for predicting outcomes of matches between two decks in the Pokemon Trading Card Game. With this tool, users can tailor their decks to specific conditions and get a calculated prediction of the match outcome beforehand.

This guide will cover the main features of the project, how to set it up, and how to use it effectively. Whether you're a beginner looking to get started, or an experienced player looking to optimize your gameplay, this guide has everything you need to know.


## Troubleshooting

Here are some common issues and their solutions:

* **Error: No module named <module name>**: This error occurs when a required module is not installed. To fix this error, install the missing module using the command `pip install <module name>`.

* **Error: Invalid version string**: This error occurs when you try to install a version of a package that doesn't exist. Check the available versions of the package using the command `pip search <package name>`, and choose a version that exists.

* **Error: Could not find a version that satisfies the requirement <package name>**: This error can occur when you try to install a package with an incorrect name. Make sure that the package name is spelled correctly and exactly matches the name on the package's PyPI page.

* **Error: Unable to import a package**: This error can occur when you have multiple versions of a package installed. To fix this error, uninstall all versions of the package using `pip uninstall <package name>`, and then reinstall the correct version using `pip install <package name>==<version>`.

If you encounter any other issues, please feel free to create an issue on the project's Github page.
## References

1. Neural networks for embeddings and representation learning: A thorough overview. (2020). https://towardsdatascience.com/neural-networks-for-embeddings-and-representation-learning-a-thorough-overview-3a6cc85bfe58

2. Keras documentation. (2022). https://keras.io/

3. Tensorflow documentation. (2022). https://www.tensorflow.org/

4. The Pokemon API. (2022). https://pokeapi.co/
## How to Contribute

Thank you for considering contributing to the TCG project! To contribute:

1. Fork the repository on Github.

2. Clone the repository to your local machine:

```
$ git clone https://github.com/<your_github_username>/tcg-project.git
```

3. Create a new branch to contain your changes:

```
$ git checkout -b <your_branch_name>
```

4. Make changes to the codebase using your favorite text editor or IDE.

5. Commit your changes and push them to your forked repository:

```
$ git add .
$ git commit -m "<a descriptive commit message>"
$ git push origin <your_branch_name>
```

6. Submit a pull request to the main repository on Github.

We appreciate your contributions to the TCG project! If you have any questions or encounter any issues while contributing, please reach out to us on the project's Github repository.
## Troubleshooting

### `pip` Command Not Found

If you receive an error message saying that the `pip` command was not found while installing the TCG project packages, you may need to install `pip` on your system. Follow these steps to install `pip`:

1. Open a terminal window.

2. Run the following command:

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
``` 

3. Run the following command to install `pip`:

```
$ sudo python get-pip.py
```

### Unable to Predict Outcome of Match

If you receive an error message saying that the outcome of the match could not be predicted, ensure that the deck files contain valid deck lists and that the deck names match those entered in the prompt.

### `module not found` Error While Running `tcg.py`

If you receive an error message saying that a module was not found while attempting to run the `tcg.py` script, ensure that you have installed all of the required packages using `pip` as described in the Installation and Running the TCG Project section of this guide. If you continue to experience issues, reach out to the project's Github repository for further assistance.
## How to Run the Machine Learning Model

To run the machine learning model for predicting outcomes of matches between two given decks, follow these steps:

1. Obtain the `decks.json`, `model.pkl`, and `predict.py` files. These can be obtained from the project's Github repository.

2. Open a terminal window and navigate to the directory containing the downloaded files.

3. Type the following command to execute the `predict.py` script with the two desired decks:

```
$ python predict.py <deck1> <deck2>
```

where `<deck1>` and `<deck2>` are the names of the decks you wish to compare. The output will include the predicted probability of each deck winning, as well as a prediction of which deck is most likely to win.

## Upgrading the Decks

The TCG project's machine learning model can be used to upgrade decks by identifying potential areas for improvement and providing suggestions for changes. To upgrade a deck, follow these steps:

1. Obtain the `decks.json`, `model.pkl`, and `train.py` files. These can be obtained from the project's Github repository.

2. Open a terminal window and navigate to the directory containing the downloaded files.

3. Type the following command to execute the `train.py` script with the desired deck file:

```
$ python train.py <deck_file>
```

where `<deck_file>` is the name of the deck file you wish to upgrade. The output will include suggestions for improvement in different categories, such as card count and energy types.

4. Make the suggested changes to the deck file.

5. Repeat steps 3 and 4 until you are satisfied with the upgraded deck.

## Requirements and Dependencies

The following are necessary requirements and dependencies for running the TCG project:

- Python 3.6 or later
- Pipenv
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
-exiftool

To install Pipenv, open a terminal window and type the following command:

```
$ pip install pipenv
```

To install the necessary packages, open a terminal window and navigate to the directory containing the downloaded files. Type the following command:

```
$ pipenv install
```

It is also important to have a general familiarity with the command-line interface (CLI) and its basic commands, such as navigating to directories, listing files, and executing scripts.

## Predicting Match Outcomes

The TCG project's machine learning model can be used to predict the outcome of a match between two given decks. To predict a match outcome, follow these steps:

1. Obtain the `decks.json` and `model.pkl` files. These can be obtained from the project's Github repository.

2. Open a terminal window and navigate to the directory containing the downloaded files.

3. Type the following command to execute the `predict.py` script with the desired deck files:

```
$ python predict.py <deck_file_1> <deck_file_2>
```

where `<deck_file_1>` and `<deck_file_2>` are the names of the deck files you wish to use. The output will be a probability score indicating the predicted outcome of the match.

## Training the Machine Learning Model

To train the machine learning model, follow these steps:

1. Organize a custom deck file for each deck you would like to use in the training set. The file must be by default in pokemontcg.io JSON format and contain the following features: name, supertype, subtype, hp, types, attacks, weaknesses, resistances, retreatCost, and artist.

2. Open a terminal window and navigate to the directory containing the downloaded files.

3. Type the following command to execute the `train_model.py` script:

```
$ python train_model.py
```

This script will randomly divide the decks into training and testing sets and train the machine learning model with the training set of decks. The trained model will then be tested with the testing set of decks to evaluate its accuracy. The resulting model will be saved as a `.pkl` file in the project directory.

## Project Structure

The TCG project directory has the following structure:

- `deck_files`: A folder containing deck files used for training and testing the machine learning model.
- `model_files`: A folder containing the trained machine learning model and other files generated during the model training process.
- `potential_names`: A text file containing a list of potential deck names for use in the deck files.
- `scripts`: A folder containing Python scripts for training the machine learning model and predicting match outcomes using custom decks.
- `test`: A folder containing unit tests for the Python scripts.
- `README.md`: A file containing general information about the project and instructions for setting up the development environment.
- `LICENSE`: A file containing the project's open-source license.
- `requirements.txt`: A file containing the necessary Python packages and their versions for running the project.
- `user_guide.md`: A file containing a user guide for using the TCG project's machine learning model.
- `decks.json`: A file containing a list of pre-defined deck files for use in predicting match outcomes. These are not used in the model training process.

## Using the Command Line Interface

The TCG project also comes with a command line interface (CLI) which allows you to input commands to the program directly in the terminal. Here are the steps to use the CLI:

1. Install the required dependencies by running:

```
pip install -r requirements.txt
```

2. Navigate to the project directory in a terminal window.

3. Type the following command to open the TCG project command prompt:

```
python cli.py
```

4. The prompt will display `tcg >` which means you are in the TCG command prompt. You can then input the following commands:

- `help`: Get a list of all available commands
- `exit`: Close the TCG command prompt
- `create deck`: Create a deck file
- `edit deck`: Edit a deck file
- `list decks`: List all available deck files
- `train model`: Train the machine learning model with custom deck files
- `predict match deck1 deck2`: Predict match outcome between two custom deck files

## Predicting Match Outcomes with Custom Decks

After training the machine learning model or using the pre-trained model, follow these steps to predict match outcomes using your custom decks:

1. Create or obtain two deck files in pokemontcg.io JSON format. Each file should contain the following features: name, supertype, subtype, hp, types, attacks, weaknesses, resistances, retreatCost, and artist.

2. Open a terminal window and navigate to the directory containing the downloaded files.

3. Type the following command to predict a match outcome between the two custom deck files:

```
$ python predict_match.py path/to/deck/file1 path/to/deck/file2
```

This will use the machine learning model to predict the outcome of a match between the two custom decks. The prediction will be printed to the terminal as a percentage of the game being won by the first deck. Note that this prediction is based on the trained machine learning model and may not always be accurate, especially if the decks are highly customized or the game mechanics change.

## Training the Machine Learning Model

To train the machine learning model with custom deck files, follow these steps:

1. Create or obtain one or more deck files in pokemontcg.io JSON format. Each file should contain the following features: name, supertype, subtype, hp, types, attacks, weaknesses, resistances, retreatCost, and artist.

2. Split your deck files into two categories: the training decks and the testing decks. The training decks will be used to train the machine learning model, while the testing decks will be used to validate the accuracy of the model. The recommended split is to use 80% of the files for training, and 20% for testing.

3. Open a terminal window and navigate to the directory containing the downloaded files.

4. Type the following command to train the machine learning model with your custom deck files:

```
$ python train_model.py path/to/training/files path/to/testing/files path/to/save/model
```

This will train the machine learning model using your custom deck files. The model will be saved to the specified path for future use. Note that the training process may take a while, depending on the number of custom deck files used and the complexity of the decks.

## File Structure

The directory structure of the TCG project is as follows:

| File/Folder | Description |
| --- | --- |
| `deck_examples/` | Example decks in pokemontcg.io JSON format |
| `models/` | Trained machine learning models in `.pkl` format |
| `potential-names/` | Potential names to be used in the custom deck files |
| `scripts/` | Scripts for training the machine learning model and upgrading the decks |
| `User Guide/` | Folder containing the user guide and other documentation |
| `.gitignore` | File specifying which files to ignore when committing to the repository |
| `predict_match.py` | Script for predicting the outcome of a match between two given decks |
| `README.md` | File containing information on the TCG project and its purpose |
| `requirements.txt` | File specifying the required packages and their versions |
| `train_model.py` | Script for training the machine learning model with custom deck files |

Note that some folders and files may not be present in your downloaded version of the repository if they are not necessary.

## Train the Machine Learning Model

If you want to train the machine learning model yourself using custom deck files, you can follow these steps:

1. Prepare your custom deck files in the JSON format used by pokemontcg.io. The files should include a list of cards with the card id and quantity. Here's an example of the format:

```
[
    {
        "id": "swshp-SWSH001",
        "quantity": 1
    },
    {
        "id": "swsh4-1",
        "quantity": 4
    },
    {
        "id": "swsh35-147",
        "quantity": 3
    },
    ...
]
```

2. Place your custom deck files in the `deck_examples` folder.

3. Type the following command to train the machine learning model using your custom deck files:

```
$ python train_model.py
```

This will train the machine learning model using your custom deck files and save the trained model in the `models` folder. The training process may take some time, depending on the number of custom deck files provided and the complexity of the decks. The details of the training process will be outputted to the terminal as the training progresses.

## Upgrade Decks

To upgrade a deck using the `upgrade_deck` script, you can follow these steps:

1. Make sure that the deck you want to upgrade is saved in the `deck_examples` folder and named `my_deck.json`.

2. Open a terminal and navigate to the directory containing the `upgrade_deck.py` script using the `cd` command.

3. Type the following command to upgrade the deck:

```
$ python upgrade_deck.py
```

This will create a new deck named `my_upgraded_deck.json` in the `deck_examples` folder with the same cards as the original deck, but with upgraded card ids and quantities as determined by the `potential-names.json` file. If a card in the original deck cannot be upgraded based on the `potential-names.json` file, it will not be included in the upgraded deck.

## Test the Machine Learning Model

To test the machine learning model using the `test_model` script, you can follow these steps:

1. Make sure that the `model.h5` file is saved in the `models` folder.

2. Prepare two deck files in the JSON format used by pokemontcg.io. The files should include a list of cards with the card id and quantity. Here's an example of the format:

```
[
    {
        "id": "swshp-SWSH001",
        "quantity": 1
    },
    {
        "id": "swsh4-1",
        "quantity": 4
    },
    {
        "id": "swsh35-147",
        "quantity": 3
    },
    ...
]
```

3. Place your deck files in the `test_examples` folder.

4. Type the following command to test the machine learning model using your deck files:

```
$ python test_model.py
```

This will predict the outcome of a match between the two decks described in the deck files and output the predicted probabilities for each possible outcome (win or loss). The results of the prediction will be outputted to the terminal.

## Train and Save the Machine Learning Model

To train and save the machine learning model with the TCG project, you can follow these steps:

1. Make sure that your training data is saved in the `training_data` folder in CSV format. The data should include columns for the card ids, quantities, and win/loss outcome (0 for loss, 1 for win). Here's an example of the format:

```
id,qty,outcome
swshp-SWSH001,1,1
swsh4-1,4,1
swsh35-147,3,0
...
```

2. Open a terminal and navigate to the directory containing the `train_model.py` script using the `cd` command.

3. Type the following command to train and save the model:

```
$ python train_model.py
```

This will train and save the model to the `models` folder with the name `model.h5`. The training process may take a few minutes depending on the size of your training data.

## Create and Format Deck Files

The TCG project requires deck files to be in the following CSV format:

```
card_id,card_qty
swshp-SWSH001,1
swsh4-1,4
swsh35-147,3
...```

To create and format your deck files, you can follow these steps:

1. Open a spreadsheet application such as Microsoft Excel or Google Sheets.

2. Create a new blank spreadsheet.

3. In the first column, enter the ids of each card you want to include in your deck (you can find these ids in the `card_ids.csv` file in the `data` folder of the TCG project repository).

4. In the second column, enter the quantity of each card you want to include in your deck.

5. Save the spreadsheet as a CSV file.

6. Repeat steps 2-5 for each deck you want to create.

7. Move your deck files to the `decks` folder in the TCG project repository.
