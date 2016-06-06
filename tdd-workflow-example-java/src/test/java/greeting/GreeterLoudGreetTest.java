package greeting;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;

import static org.junit.Assert.*;

@RunWith(Parameterized.class)
public class GreeterLoudGreetTest {
    private Greeter sut;

    public String expected;
    public String given;

    public GreeterLoudGreetTest(String expected, String given) {
        this.expected = expected;
        this.given = given;
    }

    @Parameterized.Parameters(name = "name={1}: loudGreet({1})={0}")
    public static Iterable<Object[]> data() {
        return Arrays.asList(new Object[][]{
                {"HELLO, WORLD!", "World"},
                {"HELLO, TESTS!", "Tests"},
                {"HI!", ""}
        });
    }

    @Before
    public void setUp() {
        sut = new Greeter();
    }

    @Test
    public void loudGreet() {
        assertEquals(expected, sut.loudGreet(given));
    }
}
