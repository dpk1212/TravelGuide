from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("AMADEUS_API_KEY"))  # Should print your key
