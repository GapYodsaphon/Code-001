#include <stdio.h>
void main()
{
    int tmp;
    int data[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (data[i] <= data[j])
            {
                tmp = data[i];
                data[i] = data[j];
                data[j] = tmp;
            }
        }
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d ",data[i]);
    }
}