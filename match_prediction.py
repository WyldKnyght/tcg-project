from pokemontcgsdk import Deck
import random
from typing import Dict,List


def evaluate_decks(deck_1: List[Dict[str, str]], deck_2: List[Dict[str, str]]) -> Dict[str, float]:
    win_percent_1 = 0
    win_percent_2 = 0
    for i in range(10):
        deck1 = Deck(deck_1)
        deck2 = Deck(deck_2)
        deck1.shuffle()
        deck2.shuffle()
        num_cards = min(len(deck1.cards), len(deck2.cards))
        result1 = 0
        result2 = 0
        for i in range(num_cards):
            if deck1.draw().hp > deck2.draw().hp:
                result1 += 1
            else:
                result2 += 1
        if result1 > result2:
            win_percent_1 += 0.1
        elif result2 > result1:
            win_percent_2 += 0.1
        else:
            win_percent_1 += 0.05
            win_percent_2 += 0.05
    return {'deck_1': win_percent_1, 'deck_2': win_percent_2}
