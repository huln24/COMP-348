public interface NamedObject {

    // Method to return object's name
    default String getName() {
        return this.getClass().getSimpleName();
    }
}
