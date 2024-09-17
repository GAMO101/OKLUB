import json
import requests

# Load JSON file
with open('dataClean2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Check if the loaded data is a list and get the first item
if isinstance(data, list) and len(data) > 0:
    first_item = data[0]  # First item in the list

    # Get event data
    events = first_item.get('events', [])

    # Your Telegram bot token
    token = '6928160486:AAFwy-vcEhLiUw6_mWDaykPBn90evij-WOM'
    chat_id = -1002381362019  # Telegram group ID

    # Initialize a list to store failed messages
    failed_events = []

    # Process each event
    for event in events:
        day = event.get('day', 'No Day')
        month = event.get('month', 'No Month')
        event_name = event.get('event_name', 'No Event Name')
        link = event.get('link', 'No Link')

        # Create a message with day, month, event name, and link
        message = f"Day: {day}\nMonth: {month}\nEvent Name: {event_name}\nMore Info: {link}"

        # Send the message using the Telegram API
        response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={
            'chat_id': chat_id,
            'text': message
        })

        # Check if the message was sent successfully
        if response.status_code != 200:
            failed_events.append(event_name)  # Add event name to the list of failed events

    # Print failed messages (if any)
    if failed_events:
        print("Failed to send messages for the following events:")
        for failed in failed_events:
            print(failed)
    else:
        print("All messages were successfully sent!")

else:
    print("The JSON structure is not as expected or the list is empty.")
