# Finate-state machine: day of my life

This code simulates a random day of the week for a person, with different activities and states based on the time of day and random factors.

### Description

The Person class represents a person's daily activities. The person goes through different states such as sleeping, running, eating, studying, reading, and hanging out. Each state is associated with specific actions based on the current hour.

### Usage

To use this code, follow these steps:

Import the random module.
Create an instance of the Person class, passing a day of the week as a parameter (e.g., "fr" for Friday).
Call the my_day() method on the created instance to simulate the person's activities throughout the day.


```py
import random

class Person():
    def __init__(self, day):
        # Initialize instance variables
        self.day = day
        self.weather = None
        self.current_state = self.sleeping

    def sleeping(self, hour):
        # Perform actions for the sleeping state
        # ...

    def running(self, hour):
        # Perform actions for the running state
        # ...

    def eating(self, hour):
        # Perform actions for the eating state
        # ...

    def studying(self, hour):
        # Perform actions for the studying state
        # ...

    def reading(self, hour):
        # Perform actions for the reading state
        # ...

    def hanging_out(self, hour):
        # Perform actions for the hanging_out state
        # ...

    def my_day(self):
        # Simulate the person's activities throughout the day
        # ...

# Create a Person instance and simulate the day
a = Person("fr")
a.my_day()

```

Make sure to replace the "fr" parameter with the desired day of the week abbreviation.

### States and Actions

The Person class defines several states, each associated with specific actions based on the current hour. Here's a summary of the states and their corresponding actions:

- Sleeping: The person is sleeping until 6 AM. If the weather is great at 6 AM, they transition to the running state. Otherwise, if it's raining at 7 AM, they go to eat. The actions performed during the sleeping state are printed to the console.
- Running: The person goes for a run at 7 AM. Based on random factors, they may choose to go to a specific location or another. The actions performed during the running state are printed to the console.
- Eating: The person eats breakfast at 8 AM. Based on random factors, they determine whether it's a holiday or not. If it's not a holiday, they transition to the studying state. Otherwise, they go hanging out. The actions performed during the eating state are printed to the console.
- Studying: The person studies until 10 PM. Based on random factors, they determine whether it's time for free time or if it's a holiday. If it's time for free time, they transition to reading. Otherwise, they go hanging out. The actions performed during the studying state are printed to the console.
- Reading: The person reads until 11 PM and then goes to sleep. The actions performed during the reading state are printed to the console.
- Hanging Out: The person hangs out in the city center until 11 PM and then goes to sleep. The actions performed during the hanging out state are printed to the console.

Please note that the code provided is incomplete and lacks some implementation details and error handling. Modify and complete it as needed for your specific use case.

Feel free to reach out if you have any questions or need further assistance



