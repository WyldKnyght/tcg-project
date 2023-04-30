import argparse
import json
from typing import Dict, Any, Optional
from match_prediction import evaluate_decks


def load_deck(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Loads a deck from a file path.
    Args:
    - file_path (str): the file path of the deck file
    Returns:
    - Dict[str, Any]: a dictionary containing the deck information
    """
    try:
        with open(file_path, 'r') as file:
            deck = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        with open('error.log', 'a') as file:
            file.write(str(e) + f'\nDeck loading error: {file_path}\n')
        return None
    return deck


def validate_deck(deck: Dict[str, Any]) -> bool:
    """
    Validates whether the deck dictionary is valid.
    Args:
    - deck (Dict[str, Any]): the deck dictionary to be validated.
    Returns:
    - Bool: a boolean value indicating whether the deck is valid.
    """
    if deck is None or not deck:
        return False
    if 'name' not in deck or 'Main Deck' not in deck or 'Sideboard' not in deck:
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('deck_file_1', type=str, help='file path of deck 1')
    parser.add_argument('deck_file_2', type=str, help='file path of deck 2')
    args = parser.parse_args()

    deck_1 = load_deck(args.deck_file_1)
    deck_2 = load_deck(args.deck_file_2)
    if not validate_deck(deck_1) or not validate_deck(deck_2):
        with open('error.log', 'a') as file:
            file.write(f'Invalid or corrupt decks:\nDeck 1: {args.deck_file_1}\nDeck 2: {args.deck_file_2}\n')
        print(
            'Invalid decks or format.\nPlease ensure the decks are in a valid JSON format (less than 1 MB.')
        return
    predictions = evaluate_decks(deck_1['Main Deck'], deck_2['Main Deck'])
    with open('match_prediction_results.txt', 'w') as file:
        file.write(json.dumps(predictions))
    print(f'Match Result:\n{json.dumps(predictions, indent=4)}')


if __name__ == '__main__':
    main()
