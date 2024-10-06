from ai_radio.data_collection import collector
from ai_radio.data_processing import filter, summarizer
from ai_radio.content_generation import radio_content
from ai_radio.tts import audio_generator
from ai_radio.scheduler import broadcast_scheduler

def main():
    # Collect data
    raw_data = collector.collect_data()
    
    # Filter and summarize data
    filtered_data = filter.filter_data(raw_data)
    summarized_data = summarizer.summarize_data(filtered_data)
    
    # Generate radio content
    radio_script = radio_content.generate_content(summarized_data)
    
    # Convert to audio
    audio = audio_generator.generate_audio(radio_script)
    
    # Schedule broadcast
    broadcast_scheduler.schedule_broadcast(audio)

if __name__ == "__main__":
    main()