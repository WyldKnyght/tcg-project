def evaluate_code(tcg_data):
    return [analyze_code(seq) if label else None for seq, label in tcg_data]