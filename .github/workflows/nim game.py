
import time
import os

class NimGame:
    def __init__(self):
        self.piles = [3, 5, 7]
        self.current_player = 'human'
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_piles(self):
        """Display the current state of all piles"""
        print("\n" + "="*50)
        print("           CURRENT GAME STATE")
        print("="*50)
        for i, pile in enumerate(self.piles, 1):
            stones = "●" * pile if pile > 0 else "(empty)"
            print(f"  Pile {i}: {stones} [{pile} stones]")
        print("="*50 + "\n")
    
    def calculate_nim_sum(self):
        """Calculate XOR of all pile sizes (Nim-sum)"""
        nim_sum = 0
        for pile in self.piles:
            nim_sum ^= pile
        return nim_sum
    
    def find_optimal_move(self):
        """Find the optimal move using Nim-sum strategy"""
        nim_sum = self.calculate_nim_sum()
        
        # If nim_sum is not 0, there's a winning move
        if nim_sum != 0:
            for i in range(len(self.piles)):
                target_size = self.piles[i] ^ nim_sum
                if target_size < self.piles[i]:
                    return i, self.piles[i] - target_size
        
        # If nim_sum is 0 (losing position), make any valid move
        for i in range(len(self.piles)):
            if self.piles[i] > 0:
                return i, 1
        
        return None, None
    
    def ai_move(self):
        """AI makes its move"""
        print("🤖 AI is thinking...")
        time.sleep(1)
        
        pile_index, count = self.find_optimal_move()
        
        if pile_index is not None and count is not None:
            self.piles[pile_index] -= count
            print(f"✓ AI removed {count} stone(s) from Pile {pile_index + 1}")
            time.sleep(1.5)
    
    def human_move(self):
        """Human player makes their move"""
        while True:
            try:
                # Get pile selection
                pile_input = input("Select a pile (1-3): ").strip()
                pile_index = int(pile_input) - 1
                
                if pile_index < 0 or pile_index >= len(self.piles):
                    print("❌ Invalid pile! Choose 1, 2, or 3.")
                    continue
                
                if self.piles[pile_index] == 0:
                    print("❌ That pile is empty! Choose another.")
                    continue
                
                # Get number of stones to remove
                count_input = input(f"Remove how many stones? (1-{self.piles[pile_index]}): ").strip()
                count = int(count_input)
                
                if count < 1 or count > self.piles[pile_index]:
                    print(f"❌ Invalid! You must remove between 1 and {self.piles[pile_index]} stones.")
                    continue
                
                # Valid move
                self.piles[pile_index] -= count
                print(f"✓ You removed {count} stone(s) from Pile {pile_index + 1}")
                break
                
            except ValueError:
                print("❌ Please enter a valid number!")
            except KeyboardInterrupt:
                print("\n\nGame cancelled. Thanks for playing!")
                exit()
    
    def is_game_over(self):
        """Check if all piles are empty"""
        return all(pile == 0 for pile in self.piles)
    
    def play(self):
        """Main game loop"""
        self.clear_screen()
        print("\n" + "╔" + "="*48 + "╗")
        print("║" + " "*15 + "NIM GAME" + " "*25 + "║")
        print("║" + " "*10 + "Play Against Perfect AI" + " "*15 + "║")
        print("╚" + "="*48 + "╝\n")
        
        print("📜 RULES:")
        print("  • Take turns removing stones from any single pile")
        print("  • Remove any number of stones (1+) from one pile per turn")
        print("  • The player who takes the LAST stone LOSES")
        print("  • The AI uses optimal Nim-sum strategy\n")
        
        input("Press Enter to start the game...")
        
        while True:
            self.clear_screen()
            self.display_piles()
            
            if self.is_game_over():
                if self.current_player == 'human':
                    print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
                    print("The AI took the last stone and lost!")
                else:
                    print("🤖 AI WINS!")
                    print("You took the last stone and lost.")
                break
            
            if self.current_player == 'human':
                print("👤 YOUR TURN")
                self.human_move()
                self.current_player = 'ai'
            else:
                self.ai_move()
                self.current_player = 'human'
        
        print("\n" + "="*50)
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again == 'y':
            self.__init__()
            self.play()
        else:
            print("\nThanks for playing! Goodbye! 👋")


def main():
    """Entry point of the program"""
    game = NimGame()
    game.play()


if __name__ == "__main__":
    main()
