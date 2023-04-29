def is_valid_credit_card(card_number: str) -> bool:
    """
    Checks if a credit card number is valid using the Luhn algorithm.

    Args:
        card_number: A string representing the credit card number.

    Returns:
        A boolean indicating whether the credit card number is valid.
    """
    s1 = s2 = 0
    for i, digit in enumerate(card_number[::-1]):
        if not digit.isdigit():
            return False
        digit = int(digit)
        if i % 2 == 0:
            s2 += digit
        else:
            for d in str(2 * digit):
                s1 += int(d)
    return (s1 + s2) % 10 == 0
