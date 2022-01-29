public abstract class PrintableObject implements NamedObject, Printable {

    // Returns object's name
    public String toString() {
        return this.getName();
    }

    // Print's info returned by toString in single line
    public void print() {
        System.out.println(this.toString());
    }



}
