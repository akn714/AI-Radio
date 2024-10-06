from ai_radio.config import IMPORTANCE_THRESHOLD

def filter_data(raw_data):
    """
    Filter out less important news
    """
    filtered_data = {}
    for source, data in raw_data.items():
        filtered_data[source] = [
            item for item in data
            if calculate_importance(item) >= IMPORTANCE_THRESHOLD
        ]
    return filtered_data

def calculate_importance(item):
    """
    Calculate importance of a news item
    """
    # Implement your importance calculation logic here
    return 0.8  # Placeholder value