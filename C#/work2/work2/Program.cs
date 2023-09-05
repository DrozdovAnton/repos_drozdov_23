using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace work2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int inputNum = int.Parse(Console.ReadLine());

            if (inputNum % 2 == 0)
            {
                Console.WriteLine("Полученное число четное");
            }    
            else
            {
                Console.WriteLine("Число нечетное");
            }
        }
    }
}
