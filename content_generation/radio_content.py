def generate_content(summarized_data):
    """
    Generate radio-like content from summarized data
    """
    script = "Welcome to AI Radio! Here are today's top tech stories:\n\n"
    
    for source, summaries in summarized_data.items():
        script += f"From {source.capitalize()}:\n"
        for summary in summaries:
            script += f"- {summary}\n"
        script += "\n"
    
    script += "That's all for now. Stay tuned for more updates!"
    
    return script