# stats.py - Handles Player Stats (RP, CB, CPR)

class Stats:
    def __init__(self):
        self.RP = 50  # Risk Propensity (1-100)
        self.CB = 50  # Cognitive Bias (1-100)
        self.CPR = 5  # Cognitive Pattern Recognition (1-10)

    def update(self, RP_change=0, CB_change=0, CPR_change=0):
        """
        Updates player stats while ensuring values stay within valid ranges.
        """
        self.RP = max(0, min(100, self.RP + RP_change))  # Keep RP between 0-100
        self.CB = max(0, min(100, self.CB + CB_change))  # Keep CB between 0-100
        self.CPR = max(1, min(10, self.CPR + CPR_change))  # Keep CPR between 1-10

    def get_stats(self):
        """
        Returns the current values of RP, CB, and CPR.
        """
        return {"RP": self.RP, "CB": self.CB, "CPR": self.CPR}

# Create a global stats instance
player_stats = Stats()

def update_stats(RP_change=0, CB_change=0, CPR_change=0):
    """
    Updates player stats while ensuring values stay within valid ranges.
    """
    player_stats.update(RP_change, CB_change, CPR_change)

def get_stats():
    """
    Returns the current values of RP, CB, and CPR.
    """
    return player_stats.get_stats()

# Reset stats to initial values
def reset_stats():
    """
    Resets all stats to their initial values
    """
    global player_stats
    player_stats = Stats()
