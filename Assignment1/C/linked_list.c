#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

#define DEBUG 1

#if DEBUG
#define DEBUG_MEM(msg, p)      \
    printf("%s %p\n", msg, p); \
    fflush(stdout)
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
    printf("New List is %p, next is %p\n", new_list, l);

    new_list->next = l;
    printf("New List is %p, next is %p, %p\n", new_list, new_list->next);

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

#define DEBUG_PRINT(msg) \
    printf("%s\n", msg); \
    fflush(stdout)

#define DEBUG_PRINT(msg)

typedef void (*op)(element e);

void element_print(element e)
{
    if (e.type == ATOM)
    {
        printf(" %c ", e.a);
        fflush(stdout);
    }
}

void foreach (list l, op method)
{
    if (l == NULL)
    {
        return;
    }

    method(l->el);
    printf("Printing %p; going to %p\n", l, l->next);
    fflush(stdout);
    foreach (l->next, method)
        ;
}

void traverse_print(list l)
{
    foreach (l, element_print)
        ;
}

void print(element e)
{
    if (e.type == ATOM)
    {
        DEBUG_PRINT("Atom");
        printf(" %c ", e.a);
        fflush(stdout);
    }
    else if (e.type == LIST)
    {
        if (e.l == NULL)
        {
            DEBUG_PRINT("Nil");
            printf("NIL");
            fflush(stdout);
        }
        else
        {
            DEBUG_PRINT("List Elem");
            printf("(");
            print(e.l->el);
            fflush(stdout);

            DEBUG_PRINT("List Next");
            print(lasel(e.l->next));
            fflush(stdout);
            printf(")");
        }
    }
}
