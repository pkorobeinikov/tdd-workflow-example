package greeting

import "testing"

func TestGreet(t *testing.T) {
	cases := []struct {
		expected string
		given    string
	}{
		{"Hello, World!", "World"},
		{"Hello, Tests!", "Tests"},
		{"Hi!", ""},
	}

	for _, c := range cases {
		actual := Greet(c.given)
		if c.expected != actual {
			t.Errorf("Greet(%v) = %v, expected %v", c.given, actual, c.expected)
		}
	}
}

func TestLoudGreet(t *testing.T) {
	cases := []struct {
		expected string
		given    string
	}{
		{"HI!", ""},
	}

	for _, c := range cases {
		actual := LoudGreet(c.given)
		if c.expected != actual {
			t.Errorf("LoudGreet(%v) = %v, expected %v", c.given, actual, c.expected)
		}
	}
}
