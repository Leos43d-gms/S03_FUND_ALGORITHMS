using System;
using System.Collections.Generic;
using System.Linq;
using System.Security;
using System.Text;
using System.Threading.Tasks;

namespace S01_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            EJER_6();
            Console.ReadKey();
        }
        static void EJER_1()
        {
            String nombre, carrera;
            Console.WriteLine("Su nombre es: ");
            nombre = Console.ReadLine();
            Console.WriteLine("Ingrese su carrera: ");
            carrera = Console.ReadLine();
            Console.WriteLine($"\nBienvenido al curso de Fund. de Algoritmos,{nombre} de la carrera {carrera}");
        }

        static void EJER_2()
        {
            Console.Write("\"Leonardo\"");
        }

        static void EJER_3()
        {
            Console.WriteLine("Ingrese el N1: ");
            int N1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese el N1: ");
            int N2 = int.Parse(Console.ReadLine());
            double div = (double)N1 / (double)N2;

            Console.WriteLine("\nSuma: " + (N1 + N2));
            Console.WriteLine("Resta: " + (N1 - N2));
            Console.WriteLine("Multiplicación: " + (N1 * N2));
            Console.WriteLine("División: " + div);
        }

        static void EJER_4()
        {
            Console.Write("Ingrese un numero decimal: ");
            double num = double.Parse(Console.ReadLine());

            double raiz2 = Math.Sqrt(num);
            double redo = Math.Round(num,0);
            double cubo = Math.Pow(num, 3);
            double raiz3 = Math.Pow(num, 1 / 3d);

            Console.WriteLine("\nRaiz 2: " + raiz2);
            Console.WriteLine("Redondeado: " + redo);
            Console.WriteLine("Al cubo: " + cubo);
            Console.WriteLine("Raiz 3: " + raiz3);
        }

        static void EJER_5()
        {
            Console.Write("Ingrese un numero: ");
            string num = Console.ReadLine();

            int entero = int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine("\nResto: " + (entero % 2));
            Console.WriteLine("Dividido: " + (deci / 3));
        }

        static void EJER_6()
        {
            
        }
    }
}
