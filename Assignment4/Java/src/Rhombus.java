public class Rhombus extends PrintableObject implements Shape {

    private double p;
    private double q;

    // Constructors

    Rhombus() {
        p = 0;
        q = 0;
    }

    Rhombus(double p, double q) {
        this.p = p;
        this.q = q;
    }

    // Accessors & Mutators
    public double getP() {
        return p;
    }

    public double getQ() {
        return q;
    }

    public void setP(double p) {
        this.p = p;
    }

    public void setQ(double q) {
        this.q = q;
    }

    @ Override
    public String toString() {
        return super.getName() + ", " + p + ", " + q;
    }

    public static Rhombus parse(String str) {
        String[] values = str.split(",");
        double p = Double.parseDouble(values[values.length - 2]);
        double q = Double.parseDouble(values[values.length - 1]);
        return new Rhombus(p,q);
    }

    @Override
    public double getArea() {
        return (p * q) / 2;
    }

    @Override
    public double getPerimeter() {
        return 2 * Math.sqrt(p*p + q*q);
    }

}
