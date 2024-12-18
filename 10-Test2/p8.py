def f(c):
    # Given 12 cards, return the missing one

    if len(c) == 12:

        cards = "AKQJT98765432"
        
        for card in cards:

            if card not in c:
                return card



if __name__ == "__main__":
    print(f("2345678TJQKA"))
    print(f("2K345AQJ967T"))