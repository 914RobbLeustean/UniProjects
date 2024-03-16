#include "vector.h"     
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "controller.h"
#include <assert.h>    

void testVectorInit() {
    Vector v;
    vectorInit(&v);
    assert(v.size == 0);
    assert(v.capacity > 0);
    vectorFree(&v);
}

void testAddProduct() {
    Vector v;
    vectorInit(&v);
    addOrUpdateProduct(&v, "TestProduct", "category", 1, "2024-12-31");
    assert(v.size == 1);
    assert(strcmp(v.items[0].name, "TestProduct") == 0);
    vectorFree(&v);
}

void testFindProductIndex() {
    Vector v;
    vectorInit(&v);
    addOrUpdateProduct(&v, "TestProduct", "category", 1, "2024-12-31");
    int index = findProductIndex(&v, "TestProduct", "category");
    assert(index == 0);
    vectorFree(&v);
}

void testDeleteProduct() {
    Vector v;
    vectorInit(&v);
    addOrUpdateProduct(&v, "TestProduct", "category", 1, "2024-12-31");
    deleteProduct(&v, "TestProduct", "category");
    assert(v.size == 0);
    vectorFree(&v);
}


//Function to run all tests
void runAllTests() {
    testVectorInit();
    testAddProduct();
    testFindProductIndex();
    testDeleteProduct();
    printf("All tests have passed.");
}

