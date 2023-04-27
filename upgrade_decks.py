from pokemontcgsdk import Card
from typing import Dict, List

from match_prediction import evaluate_decks


def upgrade_decks(deck_1: List[Dict[str, str]], deck_2: List[Dict[str, str]]) -> str:
    res_deck = []
    res_deck.append(deck_1)
    res_deck.append(deck_2)
    for i in range(10):
        results = evaluate_decks(deck_1, deck_2)
        diff = results['deck_1'] - results['deck_2']
        underperforming_deck_index = 1 if diff < 0 else 0
        underperforming_deck = res_deck[underperforming_deck_index]
        underperforming_card = underperforming_deck[0]
        for card in underperforming_deck:
            if card['name'] != underperforming_card['name'] and card['popularity_percent'] < underperforming_card['popularity_percent']:
                underperforming_card = card
        res_deck[underperforming_deck_index] = [card if card['name'] != underperforming_card['name'] else get_better_card(card) for card in underperforming_deck]
    return res_deck

def get_better_card(card: Dict[str,str]) -> Dict[str, str]:
    better_cards = Card.where(name=card['name']).where(page=1).where(pageSize=5).all()
    better_card = better_cards[0]
    if len(better_cards) == 1:
        return better_card
    for i in range(1, len(better_cards)):
        if better_cards[i]['popularity_percent'] > better_card['popularity_percent']:
            better_card = better_cards[i]
    return better_card

upgrade1 = upgrade_decks(deck_1, deck_2)
with open('suggestions.txt', 'w') as f:
    for deck in upgrade1:
        f.write('====Deck====\n')
        for card in deck:
            f.write(card['name'] + ':' + card['set_name'] + ':' + str(card['popularity_percent']) + '\n')
        f.write('\n')
