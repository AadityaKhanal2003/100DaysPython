print("""
 _      _            _    _            _    
| |    | |          | |  (_)          | |   
| |__  | |  __ _   ___| | ___  __ _  ___| | __
| '_ \ | | / _` | / __| |/ / |/ _` |/ __| |/ /
| |_)  | |  (_| |  (__|   <| | (_| | (__|   < 
|_.__/ |_| \__,_| \___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/   
""")

# CLI based Blackjack game
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []
def deal_cards(rd_cards):
    random_card = random.choice(rd_cards)
    return random_card
for c in range(2):
    dealer_cards = deal_cards(cards)
    computer_cards.append(dealer_cards)
for u in range(2):
    client_cards = deal_cards(cards)
    user_cards.append(client_cards)

def calculate_score():
    total_cards_comp = sum(computer_cards)
    total_cards_user = sum(user_cards)
    if (user_cards[0] == 11 and user_cards[1] == 10) or (user_cards[0] == 10 and user_cards[1] == 11):
        print(f"Blackjack !!! Client wins. Client cards: {user_cards}\n Dealer cards: {computer_cards} ")

        return 0
    elif (computer_cards[0] == 11 and computer_cards[1] == 10) or (user_cards[0] == 10 and user_cards[1] == 11):
        print(f"Dealer's Blackjack. Better luck next time. Dealer cards: {computer_cards}\n Client cards: {user_cards}")
    else:
        game_over = True
        while game_over:
            if total_cards_user < 21:
                print(
                    f' Dealer cards: {computer_cards[0]} is the first card.\n Client cards: {user_cards}, total: {total_cards_user}')
                draw_more = input("Do you want to draw one more card: (y/n)").lower()
                if draw_more == 'y':
                    new_card = deal_cards(cards)
                    user_cards.append(new_card)
                    total_cards_user = sum(user_cards)
                    if total_cards_user == 21:
                        print(f'BLACKJACK, Client cards: {user_cards} | Score: {total_cards_user} (WON)')
                        print(f'Dealer Cards: {computer_cards} | Score: {total_cards_comp} (LOST)')
                    elif total_cards_user > 21:
                        print(f'Dealer Cards: {computer_cards} | Score: {total_cards_comp} (WON)')
                        print(f'Client cards: {user_cards} | Score: {total_cards_user} (LOST)')
                        game_over = False
                    else:
                       pass
                elif draw_more == 'n':
                    if total_cards_comp < 21:
                        comp_new_card = deal_cards(cards)
                        computer_cards.append(comp_new_card)
                        total_cards_comp = sum(computer_cards)
                        print(f'Dealer revealed their card: {computer_cards}| Score: {total_cards_comp}')
                        print(f'Client cards: {user_cards}| Score: {total_cards_user}')
                    elif total_cards_comp > 21:
                        game_over = False
                        print(f'Dealer Cards: {computer_cards} | Score: {total_cards_comp} (LOST)')
                        print(f'Client cards: {user_cards} | Score: {total_cards_user} (WON)')
                    elif total_cards_comp == 21:
                        print(f'BLACKJACK, Dealer cards: {computer_cards} Score: {total_cards_comp} (WON)')
                        print(f'Client Cards: {computer_cards} | Score: {total_cards_comp} (LOST)')
                        game_over = False
                    elif total_cards_comp == total_cards_user:
                        print("DRAW!!")
                    else:
                        print(f'Client cards: {user_cards}\n Dealer cards: {computer_cards}')
                else:
                    print("Technical issue occured! Press 'r' to restart the game or 'q' to quit")
                    restart = input("What is your choice?: ").lower()
                    if restart == 'r':
                            calculate_score()
                    else:
                        game_over = False

            else:
                game_over = False
calculate_score()