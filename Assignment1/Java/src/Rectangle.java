public class Rectangle extends PrintableObject implements Shape {

    private double width;
    private double length;

    // Constructors
    Rectangle() {
        width = 0;
        length = 0;
    }

    Rectangle (double width, double length) {
        this.width = width;
        this.length = length;
    }

    // Accessors and Mutators
    public double getWidth() {
        return width;
    }

    public double getLength() {
        return length;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public void setLength(double length) {
        this.length = length;
    }

    @Override
    public String toString() {
        return getName() + ", " + length + ", " + width;
    }

    public static Rectangle parse(String str) {
        String[] values = str.split(",");
        double first = Double.parseDouble(values[values.length - 2]);
        double second = Double.parseDouble(values[values.length - 1]);
        Rectangle rectangle;
        if (first < second) {
            return new Rectangle(first, second);
        }
        else {
            return new Rectangle(second, first);
        }
    }

    @Override
    public double getArea() {
        return width * length;
    }

    @Override
    public double getPerimeter() {
        return 2 * (width + length);
    }

    // TEST
    public static void main(String[] args) {
        String str = "Rectangle,2,3.5";
        Rectangle r1 = parse(str);
        System.out.println(r1.toString());
    }

}
