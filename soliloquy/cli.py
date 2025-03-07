import os
import sys
import argparse
from soliloquy.engine import SoliloquyEngine

def main():
    """Main entry point for the Soliloquy CLI."""
    parser = argparse.ArgumentParser(description="Soliloquy Text Adventure Engine")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Run game command
    run_parser = subparsers.add_parser("run", help="Run a Soliloquy game")
    run_parser.add_argument("game_dir", help="Directory containing game YAML files")
    run_parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    # Create game command
    create_parser = subparsers.add_parser("create", help="Create a new Soliloquy game")
    create_parser.add_argument("game_name", help="Name of the new game")
    create_parser.add_argument("--destination", "-d", default=".", help="Destination directory")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle no command
    if not args.command:
        parser.print_help()
        return 1
    
    # Run a game
    if args.command == "run":
        if not os.path.isdir(args.game_dir):
            print(f"Error: Game directory '{args.game_dir}' not found.")
            return 1
        
        engine = SoliloquyEngine(args.game_dir)
        engine.start_game()
    
    # Create a new game
    elif args.command == "create":
        from soliloquy.utils.game_creator import create_new_game
        create_new_game(args.game_name, args.destination)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

