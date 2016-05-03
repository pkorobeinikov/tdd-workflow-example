<?php

namespace Greeting;

class GreeterTest extends \PHPUnit_Framework_TestCase
{
    /** @var Greeter */
    private $sut;

    protected function setUp()
    {
        $this->sut = new Greeter();
    }

    /** @dataProvider provideGreetingData */
    public function testGreet(string $expected, string $given)
    {
        static::assertEquals($expected, $this->sut->greet($given));
    }

    public function provideGreetingData()
    {
        return [
            ['expected' => 'Hello, World!', 'given' => 'World'],
            ['expected' => 'Hello, Tests!', 'given' => 'Tests'],
            ['expected' => 'Hi!', 'given' => ''],
        ];
    }

    public function testLoudGreet()
    {
        static::assertEquals('HI!', $this->sut->loudGreet(''));
    }
}
