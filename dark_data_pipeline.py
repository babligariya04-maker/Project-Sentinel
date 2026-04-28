import json
import time
import random
from datetime import datetime

# The supply chain nodes we are monitoring
NODES = ["Mumbai Port", "Pune Hub", "Nashik Hub", "Surat Factory", "Ahmedabad Plant"]

# Unstructured "Dark Data" keywords our system is looking for
KEYWORDS = ["strike", "flooded", "traffic collision", "bridge repair", "clear skies", "smooth transit"]

def generate_dark_data():
    """Simulates scraping unstructured data from local news and social media."""
    data_feed = []
    
    # Generate 5-10 recent 'events' across the network
    for _ in range(random.randint(5, 10)):
        event = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "location": random.choice(NODES),
            "keyword_flagged": random.choice(KEYWORDS),
            "raw_text_snippet": f"Local reports indicate {random.choice(KEYWORDS)} near the main transit corridor.",
            "source": random.choice(["Twitter/X API", "Local News RSS", "Telegram Logistics Channel"])
        }
        data_feed.append(event)
    
    return data_feed

def run_pipeline():
    """Runs continuously, updating the JSON file every 5 seconds."""
    print("🛡️ Project Sentinel: Dark Data Pipeline Active...")
    print("Listening for unstructured supply chain disruptions (Press Ctrl+C to stop)")
    
    try:
        while True:
            live_data = generate_dark_data()
            
            # Write the simulated scraped data to a JSON file
            with open("live_alerts.json", "w") as file:
                json.dump(live_data, file, indent=4)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Database updated with {len(live_data)} new local reports.")
            
            # Wait 5 seconds before "scraping" again
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nPipeline shut down successfully.")

if __name__ == "__main__":
    run_pipeline()