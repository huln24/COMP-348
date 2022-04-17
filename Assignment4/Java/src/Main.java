import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toMap;

public class Main {
    public static void main(String args[]) {

        System.out.println("------------------------------------------");
        System.out.println("        Welcome to Shapes Program!");
        System.out.println("------------------------------------------");

        Scanner keyIn = new Scanner(System.in);
        String filePath;

        // Ask user for path name
        System.out.println("\nPlease enter the path of the file containing the shapes: ");
        filePath = keyIn.nextLine();
        Shape[] shapes = new Shape[0];

        // Read each line of the file as stream element
        try (Stream<String> fileStream = Files.lines(Paths.get(filePath))) {
            // Convert stream of file lines to array of Shape objects
            shapes = fileStream.flatMap(shape -> Stream.of(stringToShape(shape))).toArray(Shape[]::new);
        } catch (IOException e) {
            System.out.println("\nFile you entered is not found!\n");
        }

        // Convert string of shapes into stream & get array of string of shape name and it's area
        String[] strShape = Arrays.stream(shapes).flatMap(shape -> Stream.of(shape.getName() + ", area: "+ shape.getArea())).toArray(String[]::new);
        Arrays.sort(strShape);
        Arrays.sort(strShape, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int nameCompare = (o1.substring(0, o1.indexOf("area:"))).compareTo(o2.substring(0, o2.indexOf("area:")));
                if (nameCompare != 0) {
                    return nameCompare;
                }
                String sub1 = o1.substring(o1.indexOf("area:") + 6);
                String sub2 = o2.substring(o2.indexOf("area:") + 6);
                return Double.compare(Double.parseDouble(sub1),Double.parseDouble(sub2));
            }
        });

        // Print sorted array of shape name & area
        System.out.println("\nShapes sorted by shape name and area:\n");
        Arrays.stream(strShape).forEach(System.out::println);

        // Convert string of shapes into stream & get array of string of shape name and it's perimeter
        strShape = Arrays.stream(shapes).flatMap(shape -> Stream.of(shape.getName() + ", perimeter: "+ shape.getPerimeter())).toArray(String[]::new);
        // Sort array by value of perimeter only
        Arrays.sort(strShape, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String sub1 = o1.substring(o1.indexOf("perimeter:") + 11);
                String sub2 = o2.substring(o2.indexOf("perimeter:") + 11);
                return Double.compare(Double.parseDouble(sub1),Double.parseDouble(sub2));
            }
        });

        System.out.println("\nShapes sorted by perimeter only:\n");
        Arrays.stream(strShape).forEach(System.out::println);

        Shape[] circles = Arrays.stream(shapes).filter(shape -> shape.getName().equalsIgnoreCase("circle")).toArray(Shape[]::new);
        Shape[] rectangles = Arrays.stream(shapes).filter(shape -> shape.getName().equalsIgnoreCase("rectangle")).toArray(Shape[]::new);
        Shape[] rhombuses = Arrays.stream(shapes).filter(shape -> shape.getName().equalsIgnoreCase("rhombus")).toArray(Shape[]::new);

        // Display summary
        System.out.println("\n----------------------------------");
        System.out.println("Summary Information:\n");

        System.out.println("Circles:");
        System.out.println("Average perimeter: " + Arrays.stream(circles).mapToDouble(e -> e.getPerimeter()).average().orElse(0));
        System.out.println("Average area: " + Arrays.stream(circles).mapToDouble(e -> e.getArea()).average().orElse(0));
        System.out.println("Total number of circles: " + Arrays.stream(circles).count());

        System.out.println("\nRectangles:");
        System.out.println("Average perimeter: " + Arrays.stream(rectangles).mapToDouble(e -> e.getPerimeter()).average().orElse(0));
        System.out.println("Average area: " + Arrays.stream(rectangles).mapToDouble(e -> e.getArea()).average().orElse(0));
        System.out.println("Total number of rectangles: " + Arrays.stream(rectangles).count());

        System.out.println("\nRhombuses:");
        System.out.println("Average perimeter: " + Arrays.stream(rhombuses).mapToDouble(e -> e.getPerimeter()).average().orElse(0));
        System.out.println("Average area: " + Arrays.stream(rhombuses).mapToDouble(e -> e.getArea()).average().orElse(0));
        System.out.println("Total number of rhombuses: " + Arrays.stream(rhombuses).count());


    }

    private static Shape stringToShape(String str) {
        String[] values = str.split(",");
        Shape shape;
        switch (values[0].toLowerCase()) {
            case "circle":
                shape = Circle.parse(str);
                break;
            case "rectangle":
                shape = Rectangle.parse(str);
                break;
            case "rhombus":
                shape = Rhombus.parse(str);
                break;
            default:
                shape = new Shape() {
                    @Override
                    public double getPerimeter() {
                        return 0;
                    }

                    @Override
                    public double getArea() {
                        return 0;
                    }
                };
        }
        return shape;
    }
}
