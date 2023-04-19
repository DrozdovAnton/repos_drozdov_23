using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sum
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string n; // input num
            int r; // output result

            Console.WriteLine("Введите 1-ое число: ");
            n = Console.ReadLine();

            r = Convert.ToInt32(n);

            Console.WriteLine("Введите 2-ое число: ");
            n = Console.ReadLine();

            r = r + Convert.ToInt32(n);

            Console.WriteLine("Результат сложения: " + r);
        }
    }
}
