from gui import AppGUI

# Entry point of the program
# This file demonstrates modularity: we keep the "main runner"
# separate from GUI, models, and explanations.
if __name__ == "__main__":
    app = AppGUI()
    app.run()
