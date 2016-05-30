package greeting

import (
	"fmt"
	"strings"
)

func Greet(name string) string {
	if 0 == len(name) {
		return "Hi!"
	}
	return fmt.Sprintf("Hello, %s!", name)
}

func LoudGreet(name string) string {
	return strings.ToUpper(Greet(name))
}
