package greeting;

public class Greeter {
    public String greet(String name) {
        if ("".equals(name)) {
            return "Hi!";
        }

        return "Hello, " + name + "!";
    }

    public String loudGreet(String s) {
        return greet(s).toUpperCase();
    }
}
