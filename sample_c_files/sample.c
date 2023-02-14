#include <stdio.h>

int g_var = 100;

enum State { Working = 1, Failed = 0 };

typedef struct _range_t {
    int start;
    int end;
} range_t;

void print_lucky()
{
    printf("lucky!\n");
}

int Function_one(int param1, int param2, int param3 ) /*violate rule 6.1.3 */
{
    if (param1 == 0) {
        return -1;
    }

    if (param1 == 1)
        return 0;
    /*violate rule 6.1.2, this should be an empty line */
    return 0;
}

int Function_two(int param1, int param2, int param3)
{
    return 0;
}/*violate rule 6.1.2 */
int main()
{
    int i, j = 0;
    int m = 6;
    int a = b = c = 1;

    printf("Hello, World!\n");

    switch (i) {
        case 0:
            break;
        case 1:
            {
                ++i;
            }
        default:
            break;
    }

    /*violate rule 6.1.1 */
  return 0;
}
