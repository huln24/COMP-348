#include <stdio.h>

typedef enum
{
    ATOM,
    LIST
} eltype;

typedef char atom;

struct _listnode;
typedef struct
{
    eltype type;
    union
    {
        atom a;
        struct _listnode *l;
    };
} element;

typedef struct _listnode
{
    element el;
    struct _listnode *next;
} * list;

// element e;
// e.type = LIST;
// e.l = NULL;
const element NIL = {.type = LIST, .l = NULL};

//returns an element whose content is set to atom a
element aasel(atom a)
{
    return {.type = ATOM, .a = a};
}

element lasel(list l)
{
    return {.type = LIST, .l = l};
}

element car(element e)
{
    if (e.type == LIST)
    {
        return e.l;
    }
    return NIL;
}

list cdr(element e)
{
    if (e.type == LIST && e.l->next != NULL || e.l->next->next != NULL)
    {
        return e.l->next;
    }
    return NIL;
}

// returns the cdr of the cdr of the list, represented by e
list cddr(element e)
{
    return cdr(cdr(e));
}

// Creates a new list whose car and cdr are the element e and the list l.
// The memory for the newly created list is allocated dynamically.
list cons(element e, list l)
{
}

// creates a new list whose elements are shallow copies of elements in l1 and l2, appended
list append(list l1, list l2)
{
}

// Frees all the memory previously allocated by the whole list
// (including all its elements and its inner lists)
void lfreer(list l)
{
    free(l);
}

void print(element e)
{
    if (e.type == ATOM)
    {
        printf(" %c ", e.a);
    }
    if (e.l->next == NIL)
    {
        printf(e.l.el);
    }
    else
    {
        printf(e.l.el);
        print(e.l->next);
    }
}
