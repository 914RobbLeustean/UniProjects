#pragma once

#include "vector.h"

void addOrUpdateProduct(Vector* v, const char* name, const char* category, int quantity, const char* expirationDate);
void deleteProduct(Vector* v, const char* name, const char* category);
void displayProductsFiltered(Vector* v, const char* searchString, int quantityThreshold, int filterType);

int compareByQuantityAsc(const void* a, const void* b);
int compareByQuantityDesc(const void* a, const void* b);