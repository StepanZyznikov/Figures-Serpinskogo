#include <iostream>
#include "TXLib.h"
#include <math.h>

int main ()
{
    while(!GetAsyncKeyState(VK_ESCAPE))
    {
        ///   ПЕРЕМЕННЫЕ (И НЕ ОЧЕНЬ)   ///
        cout << "Введите число вершин:";
        int a;
        cin >> a;
        cout << "Введите максимальную длину перескока:";
        int b;
        cin >> b;
        cout << "Введите два числа - расстояние от точки к которой идёт построение до следа:";
        int m1;
        cin >> m1;
        cout << "Введите два числа - расстояние от следа до старой точки:";
        int m2;
        cin >> m2;
        double Tau = 6.283184;
        int vertex[100][2] = {0};
        int x = rand() % 1000;
        int y = rand() % 1000;
        int now_vertex;
        int previous_vertex;

        ///   ПОДГОТОВКА ОКНА И ИНСТРУМЕНТОВ РИСОВАНИЯ   ///
        txCreateWindow(1000, 1000);
        txSetColor(RGB (0, 255, 0), 3);
        txCircle(x, y, 1);
        txSetColor(RGB (255, 0, 0), 1);
        txSetFillColor(RGB (255, 0, 0));
        cout << "a:" << a << "\n" << "b:" << b << "\n" << "m1:" << m1 << "\n" << "m2:" << m2 << "\n";

        ///   ПОДГОТОВКА ТОЧЕК ///
        if(a != 1)
        {
            for(int i = 0; i < a; i++)
            {
                vertex[i][0] = int(cos(Tau * i / a) * 375 + 500);
                vertex[i][1] = int(sin(Tau * i / a) * 375 + 500);
            }
        }
        else
        {
            vertex[0][0] = 500;
            vertex[0][1] = 500;
        }

        for(int i = 0; i < a; i++)
        {
            txCircle (vertex[i][0], vertex[i][1], 2);
        }

        ///   БЕСКОНЕЧНЫЙ ЦИКЛ РИСОВАНИЯ   ///
        now_vertex = rand()%a;
        x = (vertex[now_vertex][0] * m2 + x * m1)/(m1 + m2);
        y = (vertex[now_vertex][1] * m2 + y * m1)/(m1 + m2);
        previous_vertex = now_vertex;
        txSetPixel (x, y, TX_WHITE);
        while(!GetAsyncKeyState(VK_ESCAPE))
        {
            now_vertex = (rand()%(2*b+1) - 1 + previous_vertex + a) % a;
            x = (vertex[now_vertex][0] * m2 + x * m1)/(m1 + m2);
            y = (vertex[now_vertex][1] * m2 + y * m1)/(m1 + m2);
            previous_vertex = now_vertex;
            txSetPixel (x, y, TX_WHITE);
        }
    }
}
