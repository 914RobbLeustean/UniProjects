#pragma once

#ifndef CATEGORIES_H
#define CATEGORIES_H

#define MAX_NAME 100
#define CATEGORY_COUNT 4

extern const char* categories[CATEGORY_COUNT];

#endif

//Product structure
typedef struct {
    char name[MAX_NAME];
    char category[MAX_NAME];
    int quantity;
    char expirationDate[MAX_NAME];
} Product;

