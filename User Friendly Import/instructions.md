# Instructions for using the Deck Match Predictor

## Importing Decks

To import a deck, follow these steps:

1. Create a text file containing the deck list in valid JSON format.

   **Note:** The file size must be less than 1 MB.

2. Save the file in the directory where the program is located.

   **Note:** By default, the program looks for deck files in the ./decks directory.

3. Restart the program and choose the file path when prompted.

   **OR**

1. Copy the JSON-formatted deck list to the clipboard.

2. Restart the program with the --clipboard flag.

   **Note:** This will automatically create a new file for each deck in the ./decks directory.

## Interpreting Match Predictions

The program will output a JSON-formatted file containing the match prediction results. For example:

```json
{
    "win_chance": 0.55,
    "draw_chance": 0.05,
    "lose_chance": 0.4
}
```

This indicates that the first deck has a 55% chance of winning, a 5% chance of drawing, and a 40% chance of losing.