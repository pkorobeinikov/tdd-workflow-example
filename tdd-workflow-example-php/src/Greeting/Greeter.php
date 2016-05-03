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

    public function loudGreet(string $name) : string
    {
        return strtoupper($this->greet($name));
    }
}
