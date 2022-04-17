public class Circle extends PrintableObject implements Shape {

    private double radius;

    // Constructors

    Circle() {
        radius = 0;
    }

    Circle(double radius) {
        this.radius = radius;
    }

    // Accessors & Mutators

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    @ Override
    public String toString() {
        return super.getName() + ", " + radius;
    }

    public static Circle parse(String str) {
        String[] values = str.split(",");
        double r = Double.parseDouble(values[values.length - 1]);
        return new Circle(r);
    }

    @Override
    public double getArea() {
        return Math.PI * Math.pow(radius, 2);
    }

    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public String getName() {
        return this.getClass().getName().toUpperCase();
    }

    // TEST
    public static void main(String[] args) {
        String str = "Circle, 2";
        Circle r1 = parse(str);
        System.out.println(r1.toString());
        System.out.println(r1.getName());
    }
}
