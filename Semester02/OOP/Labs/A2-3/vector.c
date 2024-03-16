#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "vector.h"

//Implementations of vectorInit, vectorAdd, vectorDelete, vectorFree, and findProductIndex

void vectorInit(Vector* v) {
    /*Initializes a Vector by setting its initial capacity and size, and allocates memory for its items
    Parameters:
            v: A pointer to a Vector instance to initialize.
    Returns: Nothing (void). Initializes the given vector*/

    v->capacity = 10;
    v->size = 0;
    v->items = malloc(v->capacity * sizeof(Product));
}

void vectorResize(Vector* v, int capacity) {
    /*Resizes the Vector's internal array to the specified capacity, adjusting the allocated memory as needed
     Parameters:
            v: A pointer to the Vector whose capacity is to be resized
            capacity: The new capacity for the vector
    Returns: Nothing (void). Resizes the internal array of the vector*/


    Product* items = realloc(v->items, sizeof(Product) * capacity);
    if (items) {
        v->items = items;
        v->capacity = capacity;
    }
}

void vectorAdd(Vector* v, const Product* item) {
    /*Adds a new Product to the Vector. If the vector is full, it resizes the internal array before adding the new item
     Parameters:
           v: A pointer to the vector where the item will be added
           item: A pointer to the Product to be added to the vector
     Returns: Nothing (void). Adds a product to the vector, resizing if necessary*/

    if (v->size == v->capacity) {
        vectorResize(v, v->capacity * 2);
    }
    v->items[v->size++] = *item;
}

void vectorDelete(Vector* v, int index) {
    /*Removes a Product from the Vector at the specified index, shifting subsequent elements to fill the gap
     Parameters:
           v: A pointer to the vector from which the item will be deleted
           index: The index of the item to delete from the vector
     Returns: Nothing (void). Deletes a product from the vector and compacts the array*/

    if (index < 0 || index >= v->size) return;
    for (int i = index; i < v->size - 1; ++i) {
        v->items[i] = v->items[i + 1];
    }
    --v->size;
}

void vectorFree(Vector* v) {
    /*Frees the memory allocated for the Vector's items, effectively cleaning up resources when the vector is no longer needed
     Parameters:
           v: A pointer to the vector to be freed
     Returns: Nothing (void). Frees the memory allocated for the vector's items*/

    free(v->items);
}

int findProductIndex(Vector* v, const char* name, const char* category) {
    /*Searches for a Product in the Vector by name and category, returning its index or -1 if not found
     Parameters:
           v: A pointer to the vector where to search for the product
           name: The name of the product to find
           category: The category of the product to find
     Returns: int. The index of the found product or -1 if not found*/

    for (int i = 0; i < v->size; ++i) {
        if (strcmp(v->items[i].name, name) == 0 && strcmp(v->items[i].category, category) == 0) {
            return i;
        }
    }
    return -1;
}