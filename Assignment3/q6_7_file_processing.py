from q5_shape import Shape, Circle, Rhombus, Ellipse


def main(file=None):
    # Get content of file containing shapes and store in file object
    if file is None:
        file = open("shapes.txt", "r")

    # Read all lines of the file and return list of strings
    s_info = file.readlines()

    # Construct shape objects from string and store as list of shapes
    shapes = []
    for line in s_info:
        shapes.append(construct_shape(line))

    # For each shape call print method
    # If shape is ellipse or rhombus print linear eccentricity or in-radius, respectively
    # In case of error with shape parameters, error message is displayed
    # q7: count occurence of each shape
    count_names = dict()
    for i in shapes:
        name = type(i).__name__
        # q7: If name of shape is already in dictionary update count
        #       else, create new element
        if name in count_names:
            count_names[name] += 1
        else:
            count_names[name] = 1

        if name != "Shape" and i.area() is None:
            print("Error: Invalid " + name)
        i.print()
        if name == "Ellipse" and i.area() is not None:
            print("   linear eccentricity: %.5f" % i.eccentricity())
        elif name == "Rhombus" and i.area() is not None:
            print("   in-radius: %.5f" % i.inradius())

    print_statistics(count_names)


# Takes dictionary of shape names and it's count & prints the statistics of count
def print_statistics(count_names):
    print("\n\nStatistics:")
    print("   Circle(s): ", count_names["Circle"])
    print("   Ellipse(s): ", count_names["Ellipse"])
    print("   Rhombus(es): ", count_names["Rhombus"])
    print("   --")
    print("   Shape(s): ", sum(count_names.values()), "\n")


# Counstructs a shape object based on shape name and values
def construct_shape(str):
    # Convert the string containing the line data into list of shape info
    # e.g. [name, arg1, arg2]
    shape = str.split(" ")

    # Create the shape based on information and return the shape object
    name = shape[0].lower().strip()
    if name == "shape":
        return Shape()
    elif name == "circle":
        return Circle(float(shape[1]))
    elif name == "ellipse":
        return Ellipse(float(shape[1]), float(shape[2]))
    elif name == "rhombus":
        return Rhombus(float(shape[1]), float(shape[2]))


# TESTS


def test_main():
    class FakeFile:
        def readlines(self):
            return ["shape", "rhombus 10 20"]

    main(FakeFile())


def test_file_process():
    assert type(construct_shape("shape")) is Shape
    assert type(construct_shape("rhombus 10 20")) is Rhombus
    assert type(construct_shape("circle 2")) is Circle
    assert type(construct_shape("Ellipse 2 4")) is Ellipse
    assert construct_shape("Ellipse -1 4").area() is None


if __name__ == "__main__":
    main()
    # $ python q2_lucas_sequence.py
    # $ coverage run -m pytest q2_lucas_sequence.py
    # $ coverage report
