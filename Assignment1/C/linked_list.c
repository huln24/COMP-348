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

const element NIL = {.type = LIST, .l = NULL};

element aasel(atom a)
{
}

element lasel(list l)
{
}

element car(element e)
{
}

list cdr(element e)
{
}

// returns the cdr of the cdr of the list, represented by e
list cddr(element e)
{
    return cdr(e);
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
}

void print(element e)
{
}
