#pragma once

#include "product.h"

typedef struct {
    Product* items;
    int size;
    int capacity;
} Vector;

void vectorInit(Vector* v);
void vectorAdd(Vector* v, const Product* item);
void vectorDelete(Vector* v, int index);
void vectorFree(Vector* v);
int findProductIndex(Vector* v, const char* name, const char* category);