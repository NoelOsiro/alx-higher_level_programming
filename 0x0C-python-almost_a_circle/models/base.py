#!/usr/bin/python3
"""Module for the Base class."""
import json
import csv
import turtle


class Base:
    """Base class for managing id attribute in future classes."""

    # Private class attribute to keep track of the number of objects.
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique id.

        Args:
            id (int, optional): The id to assign to the instance.
            Defaults to None.

        Note:
            If id is provided, it will be assigned to the instance.
            If id is not provided, __nb_objects will be incremented, and
            the new value will be assigned to the instance as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries
            to be converted to JSON.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def from_json_string(cls, json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representing
            a list of dictionaries.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of
        list_objs to a file.

        Args:
            list_objs (list): A list of instances that
            inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_string = "[]"

        if list_objs is not None:
            # Create a list of dictionaries representing the objects
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)

                for dictionary in json_list:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)

            return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes
        set from a dictionary.

        Args:
            **dictionary: A dictionary containing
            attribute names and values.

        Returns:
            Base: An instance with attributes
            set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes
        set from a dictionary.

        Args:
            **dictionary: A dictionary containing
            attribute names and values.

        Returns:
            Base: An instance with attributes
            set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of objects to a CSV file.

        Args:
            list_objs (list): A list of instances
            that inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            writer.writerow(fieldnames)

            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fieldnames])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of instances from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if cls.__name__ == "Rectangle": 
                        instance = cls(int(row['width']), int(row['height']),
                                       int(row['x']), int(row['y']), int(row['id']))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row['size']),
                                       int(row['x']), int(row['y']), int(row['id']))

                    instance_list.append(instance)

            return instance_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw rectangles
        and squares using Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        window = turtle.Screen()
        window.title("Turtle Drawing")
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(0)  # Set the drawing speed (0 is the fastest)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        pen.hideturtle()
        turtle.done()
