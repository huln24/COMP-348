#include <stdio.h>
#include "linked_list.h"
#include <stdlib.h>

void test_cons();
void test_aasel();
void test();

int main(int argc, const char *argv[])
{
    test_aasel();
    test_cons();
    test();

    return 0;
}

void test()
{
    printf("------TEST START --------\n");
    list l1 = cons(aasel('a'), NULL);
    list l2 = cons(aasel('b'), l1);
    list l3 = cons(aasel('c'), NULL);
    print(lasel(l1));
    printf("\n");
    print(lasel(l2));
    printf("\n");
    print(lasel(l3));
    printf("\n");
    fflush(stdout);

    list l4 = append(l2, l3);
    print(lasel(l4));
    lfreer(l4);
}

void test_aasel()
{
    print(aasel('a'));
    printf("\n");
    print(lasel(NULL));
    printf("\n");
}

void test_cons()
{
    list a = cons(aasel('a'), NULL);

    print(lasel(a));
    printf("\n");

    lfreer(a);
}
