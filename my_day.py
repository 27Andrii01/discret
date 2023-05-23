"""
Module describe my random day of the week 
"""
import random

class Person():
    """
    Represents a person and their daily activities.
    """
    def __init__(self, day) -> None:
        """
        Initializes a Person object.

        Args:
            day (str): The day of the week abbreviation.
        """
        self.day = day
        self.weather = None
        self.current_state = self.sleeping

    def sleeping(self, hour):
        """
        Performs actions for the sleeping state.

        Args:
            hour (int): The current hour of the day.
        """
        print(f"{hour}: I am sleeping")
        cir = random.randrange(1, 3)
        if hour == 6 and cir == 1:
            print(f"{hour}: The weather is great ")
            self.current_state = self.running
        elif hour == 7:
            print(f"{hour}: Its rainig now, so i won't run. I will go to trapezna")
            self.current_state = self.eating

    def running(self, hour):
        """
        Performs actions for the running state.

        Args:
            hour (int): The current hour of the day.
        """
        print(f"{hour}: I am running")
        cir = random.randrange(1, 3)
        if hour == 7 and cir == 2:
            print(f"{hour}: There is no english breakfast in trapezna, I will go to 7/23")
            self.current_state = self.eating
        elif hour == 7 and cir == 1:
            print(f"{hour}: I wil go to trapezna")
            self.current_state = self.eating

    def eating(self, hour):
        """
        Performs actions for the eating state.

        Args:
            hour (int): The current hour of the day.
        """
        print(f"{hour}: I am eating")
        cir = random.randrange(1, 8)
        if (hour == 8 and cir != 6) or (hour == 8 and cir != 7):
            print("Today it is not a holiday")
            self.current_state = self.studying
        elif (hour == 8 and cir == 6) or (hour == 8 and cir == 7):
            print("Today it is a holiday")
            self.current_state = self.hanging_out

    def studying(self, hour):
        """
        Performs actions for the studying state.

        Args:
            hour (int): The current hour of the day.
        """
        print(f"{hour}: I'm studying")
        cir = random.randrange(1, 8)
        if (hour == 22 and cir != 6) or (hour == 22 and cir != 7):
            print(f"{hour}: It is time to have some free time")
            self.current_state = self.reading
        elif (hour == 19 and cir == 6) or (hour == 19 and cir == 7):
            print(f"{hour}: Today it is a holiday")
            self.current_state = self.hanging_out

    def reading(self, hour):
        """
        Performs actions for the reading state.

        Args:
            hour (int): The current hour of the day.
        """
        print(f"{hour}: I'm reading")
        if hour == 23:
            print(f"{hour}: It is time to sleep")
            self.current_state = self.sleeping

    def hanging_out(self, hour):
        """
        Performs actions for the hanging out state.

        Args:
            hour (int): The current hour of the day.
        """
        print(f"{hour}: I'm in the city center")
        if hour == 23:
            print(f"{hour}: It is time to sleep")
            self.current_state = self.sleeping

    def my_day(self):
        """
        Simulates the person's activities throughout the day.
        """
        for hour in range(1, 25):
            self.current_state(hour)

a = Person("fr")
a.my_day()
