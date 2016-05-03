<?php

namespace Greeting;

final class Greeter
{

    public function greet(string $name) : string
    {
        if ('' === $name) {
            return 'Hi!';
        }

        return "Hello, $name!";
    }
}
