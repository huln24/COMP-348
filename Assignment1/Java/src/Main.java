//----------------------------------
// COMP 348, Section
// Khulan Ulziibat, 40078465
// Winter 2022
//----------------------------------

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        System.out.println("------------------------------------------");
        System.out.println("        Welcome to Shapes Program!");
        System.out.println("------------------------------------------");

        Scanner keyIn = new Scanner(System.in);
        String filePath;

        // Ask user for path name
        System.out.println("\nPlease enter the path of the file containing the shapes: ");
        filePath = keyIn.nextLine();
        File file = new File(filePath);

        Shape[] shapes = parseFile(file);

        System.out.println("\nShapes before sorting:\n");
        Printable.print(java.util.Arrays.copyOf(shapes, shapes.length, Printable[].class));
        System.out.println("-----------------------------");

        // Sort the array of shapes
        // Using anonymous Comparator class
        Arrays.sort(shapes, new Comparator<Shape>() {
            @Override
            public int compare(Shape s1, Shape s2) {
                int name = compareName(s1.getName(), s2.getName());
                int area = Double.compare(s1.getArea(), s2.getArea());
                if (name == 0) {
                    return area;
                }
                return name;
            }
        });

        System.out.println("\nShapes after sorting:\n");
        Printable.print(java.util.Arrays.copyOf(shapes, shapes.length, Printable[].class));

        keyIn.close();
    }

    // Count number of lines in the file and return it
    public static int countLines(File file) {
        int lines = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            // Get number of lines in the file
            while (br.readLine() != null) {
                lines++;
            }
        } catch (IOException e) {
            System.out.println("\nFile you entered is not found!\n");
            System.out.println("Closing the program ...\n");
        }
        return lines;
    }

    // Parse the file containing shapes and return array of Shape objects
    public static Shape[] parseFile(File file) {
        // Get number of line = number of shapes
        int lines = countLines(file);

        Shape[] shapes = new Shape[lines];
        // Try-with-resources to open file
        // Closes file automatically when exiting try block
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {

            // Read line by line
            // Create object of appropriate shape type & add to array of shapes
            String line;
            int i = 0;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");

                if (values[0].equalsIgnoreCase("circle")) {
                    shapes[i] = Circle.parse(line);
                } else if (values[0].equalsIgnoreCase("rectangle")) {
                    shapes[i] = Rectangle.parse(line);
                }
                i++;
            }
        } catch (IOException e) {
            System.out.println("\nFile you entered is not found!\n");
            System.out.println("Closing the program ...\n");
            e.printStackTrace();
        }
        return shapes;
    }

    // Compare 2 string names
    public static int compareName(String name1, String name2) {
        for (int i = 0; i < name1.length() || i < name2.length(); i++) {
            if (name1.charAt(i) == name2.charAt(i)) {
                continue;
            } else if (name1.charAt(i) < name2.charAt(i)) {
                return -1;
            } else if (name1.charAt(i) > name2.charAt(i)) {
                return 1;
            }
        }
        // When both name has same letters after the loop
        // the name with extra letters is considered larger
        if (name1.length() < name2.length()) {
            return -1;
        } else if (name1.length() == name2.length()) {
            return 0;
        } else {
            return 1;
        }
    }
}
