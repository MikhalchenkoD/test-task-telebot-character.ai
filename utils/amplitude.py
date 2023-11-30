import json
import aiohttp
from config_data.config import AMPLITUDE_API_KEY

async def post_amplitude_info(user_id, event):
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }

    data = {
        "api_key": AMPLITUDE_API_KEY,
        "events": [{
            "user_id": user_id,
            "event_type": event
        }]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('https://api2.amplitude.com/2/httpapi', headers=headers,
                                data=json.dumps(data)) as response:
            return await response.json()