using System;

public static class HelloWorld
{
  public static void Main(string[] args)
  {
    // write console
    Console.WriteLine("Hello World");
    // read console
    Console.WriteLine("input number :");
    string str = Console.ReadLine();
    double mass = Convert.ToDouble(str);
    Console.WriteLine(mass);
  }
}
