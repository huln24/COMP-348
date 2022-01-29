import java.util.Iterator;
import java.util.List;

public interface Printable {

    // Print object's info to the console
    void print();

    // Receive list of Printable items and calls their print method
    static void print(Printable... items) {

        for (Printable item: items) {
            item.print();
        }
    }
}
