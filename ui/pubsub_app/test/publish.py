import json
import base64
from datetime import datetime, timezone

# 1. Define the inner data structure
inner_data = {
    "time_series_id": "ts_sensor_alpha_001",
    "timestamp": datetime.now(timezone.utc).isoformat(), # Example: "2024-08-01T12:30:45.123456+00:00"
    "target_value": 75.5,
    "temperature_unit": "Fahrenheit",
    "humidity": 45.2,
    "battery_level": 88.9,
    "location": "Warehouse Section B, Rack 3",
    "status": "operational",
    "received_at": datetime.now(timezone.utc).isoformat(), # Example: "2024-08-01T12:31:00.567890+00:00"
    "metadata": {
        "sensor_model": "XYZ-2000",
        "firmware_version": "1.2.3",
        "calibration_date": "2024-01-15"
    }
}

# 2. Convert the inner data to a JSON string
inner_data_json_string = json.dumps(inner_data, indent=2)

# 3. Base64 encode the JSON string
#    The string needs to be encoded to bytes first (e.g., UTF-8)
base64_encoded_data = base64.b64encode(inner_data_json_string.encode('utf-8')).decode('utf-8')

# 4. Construct the full Pub/Sub message
pubsub_message = {
  "message": {
    "data": base64_encoded_data,
    "messageId": "auto-generated-id-12345", # Or any unique ID
    "publishTime": datetime.now(timezone.utc).isoformat() # Or a specific publish time
  },
  "subscription": "projects/secpatch-460620/subscriptions/iot-realtime-subscription" # Example subscription
}

# To see the final message:
print(json.dumps(pubsub_message, indent=2))

# To see the decoded data (for verification):
# decoded_verify = base64.b64decode(base64_encoded_data).decode('utf-8')
# print("\nDecoded data for verification:")
# print(decoded_verify)
