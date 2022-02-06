#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

#define DEBUG 1

#if DEBUG
#define DEBUG_MEM(msg, p) printf("%s %p\n", msg, p)
#else
#define DEBUG_MEM(msg)
#endif

const element NIL = {.type = LIST, .l = NULL};

//returns an element whose content is set to atom a
element aasel(atom a)
{
    element a1 = {.type = ATOM, .a = a};
    return a1;
}

// returns an element whose content is set to list l
element lasel(list l)
{
    element l1 = {.type = LIST, .l = l};
    return l1;
}

// returns the head of the list, represented by e
// returns NIL, if e is not a list
element car(element e)
{
    if (e.type == LIST)
    {
        return e.l->el;
    }
    return NIL;
}

// Returns tail of the list, represented by e.
// The tail of a list with one or zero element is NIL.
// The tail of an element that is not a list is also NIL.
list cdr(element e)
{
    if (e.type == LIST && (e.l != NULL || e.l->next != NULL))
    {
        return e.l->next;
    }
    return NULL;
}

// returns the cdr of the cdr of the list, represented by e
list cddr(element e)
{
    return cdr((cdr(e))->el);
}

// Creates a new list whose car and cdr are the element e and the list l.
// The memory for the newly created list is allocated dynamically.
list cons(element e, list l)
{

    list new_list = (list)malloc(sizeof(list));
    DEBUG_MEM("malloc", new_list);

    new_list->el = e;
    new_list->next = l;
    return new_list;
}

// creates a new list whose elements are shallow copies of elements in l1 and l2, appended
list append(list l1, list l2)
{
    list app_list = l1;
    while (app_list != NULL)
    {
        app_list = app_list->next;
        if (app_list->next == NULL)
        {
            app_list->next = l2;
            break;
        }
    }
    return app_list;
}

// Frees all the memory previously allocated by the whole list
// (including all its elements and its inner lists)
void lfreer(list l)
{
    list n = l;

    while (n != NULL)
    {
        list p = n;
        n = n->next;

        DEBUG_MEM("Freeing", p);
        free(p);
    };
}

void print(element e)
{
    if (e.type == ATOM)
    {
        printf(" %c ", e.a);
    }
    else if (e.type == LIST)
    {
        if (e.l == NULL)
        {
            printf("NIL");
        }
        else
        {
            printf("(");
            print(e.l->el);

            print(lasel(e.l->next));
            printf(")");
        }
    }
}
