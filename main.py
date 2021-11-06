import random


def black_jack():
    host_total = 0
    host_show = 0
    player = 0
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    player_bust = False
    host_bust = False
    player_jack = False

    for card in range(2):
        player_card_index = random.randint(0, len(cards) - 1)
        player += cards[player_card_index]  # Add the points first
        cards.pop(player_card_index)  # or it pops out and then goes error
        host_card_index = random.randint(0, len(cards)-1)
        host_total += cards[host_card_index]
        if card == 1:
            host_show += cards[host_card_index]
            # for showing only the second card to player
        cards.pop(host_card_index)

    print(f"host points {host_show}")
    print(f"Your points {player}")
    if player == 21:
        print("Geez, You got Black Jack @@")
        player_jack = True

    ask_a_hit = True
    while ask_a_hit is True and player_jack is False:
        player_input = input("\nHit or stand? 'hit'/'stand'\n").lower()
        while player_input != "hit" and player_input != "stand":
            print("Invalid input")
            player_input = input("Hit or stand?\n").lower()
        if player_input == "hit":
            player_card_index = random.randint(0, len(cards) - 1)
            player += cards[player_card_index]
            print(f"\nYou got {cards[player_card_index]}, {player} points now")
            cards.pop(player_card_index)
            if player > 21:
                print(f"{player} points, you bust :(")
                player_bust = True
                break
        else:
            ask_a_hit = False
    if player_bust is not True:
        if host_total == 21:
            print("Bad, bad host got Black Jack!")
        while host_total < 17:
            host_card_index = random.randint(0, len(cards) - 1)
            host_total += cards[host_card_index]
            print(f"Host got a {cards[host_card_index]}, now {host_total} points")
            cards.pop(host_card_index)
            if host_total > 21:
                print(f"Oh oh points {host_total}, host bust")
                host_bust = True
                break

        if host_bust is True:
            print("You win!")
        elif player > host_total:
            print(f"Host total {host_total}")
            print("You win!")
        elif player == host_total:
            print(f"Host total {host_total}")
            print("Push!")
        else:
            print(f"Host got {host_total}")
            print("You lose:(")


again = True
print("This is a simple Black Jack game :)")
print("Cut the nonsense, let's play!\n")

while again is True:
    black_jack()
    keep_playing = input("\nStart a new game? y/n\n").lower()
    if keep_playing != "y":
        again = False

print("OK, bye!")
