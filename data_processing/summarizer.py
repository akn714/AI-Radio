from ai_radio.config import SUMMARY_LENGTH

def summarize_data(filtered_data):
    """
    Generate summaries for the filtered news
    """
    summarized_data = {}
    for source, data in filtered_data.items():
        summarized_data[source] = [
            generate_summary(item) for item in data
        ]
    return summarized_data

def generate_summary(item):
    """
    Generate a summary for a single news item
    """
    # Implement your summarization logic here
    return f"Summary of {item['title']}"[:SUMMARY_LENGTH]