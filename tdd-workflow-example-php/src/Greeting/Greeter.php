<?php

namespace Greeting;

final class Greeter
{

    public function greet(string $name) : string
    {
        return "Hello, $name!";
    }
}
