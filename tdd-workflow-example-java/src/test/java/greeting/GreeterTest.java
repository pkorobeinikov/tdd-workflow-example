package greeting;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;

import static org.junit.Assert.*;

@RunWith(Parameterized.class)
public class GreeterTest {
    private Greeter sut;

    public String expected;
    public String given;

    public GreeterTest(String expected, String given) {
        this.expected = expected;
        this.given = given;
    }

    @Parameterized.Parameters(name = "name={1}: greet({1})={0}")
    public static Iterable<Object[]> data() {
        return Arrays.asList(new Object[][]{
                {"Hello, World!", "World"},
                {"Hello, Tests!", "Tests"},
                {"Hi!", ""}
        });
    }

    @Before
    public void setUp() {
        sut = new Greeter();
    }

    @Test
    public void greet() {
        assertEquals(expected, sut.greet(given));
    }

    @Test
    public void loudGreet() {
        assertEquals(expected.toUpperCase(), sut.loudGreet(given));
    }
}
