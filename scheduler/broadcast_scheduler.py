import schedule
import time
from ai_radio.config import BROADCAST_INTERVAL

def schedule_broadcast(audio):
    """
    Schedule the broadcast of the generated audio
    """
    schedule.every(BROADCAST_INTERVAL).seconds.do(broadcast, audio)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

def broadcast(audio):
    """
    Simulate broadcasting the audio
    """
    print("Broadcasting news update...")
    # Implement your broadcasting logic here
    # For example, you might want to stream the audio or save it to a file