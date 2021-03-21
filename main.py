def load_card_db() -> dict:
    """
    Načtení databáze všech existujících karet ze souboru txt

    :return: dictionary
    """
    with open("cards.txt", "r") as file:
        content = file.read()
    return eval(content)


card_db = load_card_db()
print(card_db)
