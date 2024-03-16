#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "controller.h"

//Implementations of addOrUpdateProduct, deleteProduct, and displayProducts

void addOrUpdateProduct(Vector* v, const char* name, const char* category, int quantity, const char* expirationDate) {
    /*Adds a new product to the vector or updates an existing one based on name and category
     Parameters:
           v: A pointer to the vector where the product will be added or updated
           name: The name of the product
           category: The category of the product
           quantity: The quantity of the product
           expirationDate: The expiration date of the product
     Returns: Nothing (void). Adds a new product or updates an existing one in the vector*/

    int index = findProductIndex(v, name, category);
    if (index != -1) { // Product exists, update it
        v->items[index].quantity += quantity;
        strcpy(v->items[index].expirationDate, expirationDate);
    }
    else { // New product
        Product newProduct;
        strcpy(newProduct.name, name);
        strcpy(newProduct.category, category);
        newProduct.quantity = quantity;
        strcpy(newProduct.expirationDate, expirationDate);
        vectorAdd(v, &newProduct);
    }
}

void deleteProduct(Vector* v, const char* name, const char* category) {
    /*Deletes a product from the vector based on name and category
     Parameters:
           v: A pointer to the vector from which the product will be deleted
           name: The name of the product to delete
           category: The category of the product to delete
     Returns: Nothing (void). Deletes a product from the vector*/

    int index = findProductIndex(v, name, category);
    if (index != -1) {
        vectorDelete(v, index);
    }
}

int compareByQuantityAsc(const void* a, const void* b) {
    /*A comparator function for qsort, comparing two Product structures by their quantity
     Parameters:
             a: A pointer to the first Product structure for comparison
             b: A pointer to the second Product structure for comparison
     Returns: int. Negative if a is less than b, zero if they are equal, and positive if a is greater than b, based on quantity*/

    const Product* productA = (const Product*)a;
    const Product* productB = (const Product*)b;
    return productA->quantity - productB->quantity;
}

int compareByQuantityDesc(const void* a, const void* b) {
    /*A comparator function for qsort, comparing two Product structures by their quantity
      Parameters:
              a: A pointer to the first Product structure for comparison
              b: A pointer to the second Product structure for comparison
      Returns: int. Negative if a is less than b, zero if they are equal, and positive if a is greater than b, based on quantity*/

    const Product* productA = (const Product*)a;
    const Product* productB = (const Product*)b;
    return productB->quantity - productA->quantity;
}

void displayProductsFiltered(Vector* v, const char* searchString, int quantityThreshold, int filterType, int (*compare)(const void*, const void*)) {
    /*Displays products from the vector that match a given search string, sorting them by quantity
     Parameters:
           v: A pointer to the vector containing products to display
           searchString: The string to filter products by. If empty, all products are displayed
           FilterType: integer to decide which filter to use
           compare: a pointer to a comparator function
     Returns: Nothing (void). Displays filtered and sorted products*/

    Product* filteredProducts = malloc(v->size * sizeof(Product));
    int count = 0;

    //Filter products based on filter type
    for (int i = 0; i < v->size; ++i) {
        int includeProduct = 0;

        if (filterType == 1) { // Filter by search string
            includeProduct = strstr(v->items[i].name, searchString) != NULL;
        }
        else if (filterType == 2) { // Filter by quantity threshold
            includeProduct = v->items[i].quantity <= quantityThreshold;
        }

        if (includeProduct) {
            filteredProducts[count++] = v->items[i];
        }
    }

    //Sort the filtered products by quantity in ascending order
    qsort(filteredProducts, count, sizeof(Product), compare);

    //Display the filtered and sorted products
    for (int i = 0; i < count; ++i) {
        printf("Name: %s, Category: %s, Quantity: %d, Expiration date: %s\n",
            filteredProducts[i].name, filteredProducts[i].category, filteredProducts[i].quantity, filteredProducts[i].expirationDate);
    }

    free(filteredProducts);
}

int daysUntilExpiration(const char* expirationDate) {
    /*Calculates the number of days from the current date until a given expiration date
     Parameters:
            expirationDate (const char*): A string representing the expiration date of a product, formatted as "YYYY-MM-DD"
     Returns:
            int: The number of days from the current date until the expiration date. If the product is already expired, it will return a negative number
     This function parses the expiration date from a string and calculates the time difference from the current date
     It adjusts the parsed date to match the struct tm format and then uses difftime to compute the difference in seconds, which it converts to days*/

    struct tm expDate = { 0 };
    time_t now = time(NULL);
    double seconds;

    //Parse the date manually using sscanf
    sscanf(expirationDate, "%d-%d-%d",
        &expDate.tm_year, &expDate.tm_mon, &expDate.tm_mday);

    //Adjust the year and month values
    expDate.tm_year -= 1900;
    expDate.tm_mon -= 1;
    expDate.tm_mday -= 1;
    expDate.tm_hour = 0;
    expDate.tm_min = 0;
    expDate.tm_sec = 0;
    expDate.tm_isdst = -1; // Let mktime handle daylight saving time

    //Calculate the difference in seconds
    seconds = difftime(mktime(&expDate), now);

    //Convert seconds to days
    return (int)(seconds / (60 * 60 * 24));
}

int isExpiringInXDays(const char* expirationDate, int x) {
    /*Determines if a product's expiration date is within a specified number of days from the current date.
     Parameters:
           expirationDate (const char*): A string representing the expiration date of a product, formatted as "YYYY-MM-DD"
           x (int): The number of days within which to check if the product expires
     Returns:
           int: Returns 1 (true) if the product expires within the next x days, or 0 (false) if it does not*/

    int days = daysUntilExpiration(expirationDate);
    return days <= x && days >= 0;
}

void displayProductsByCategoryAndExpiration(Vector* v, const char* category, int daysUntilExp) {
    /*Displays a list of products of a specified category that are expiring within a specified number of days
     Parameters:
           v (Vector*): A pointer to a Vector containing a list of products
           category (const char*): The category of products to filter by. If an empty string is passed, all categories will be considered
           daysUntilExp (int): The number of days within which products are considered to be expiring soon
     Returns:
            Nothing (void)*/

    time_t now;
    time(&now); // Get current time for comparison

    for (int i = 0; i < v->size; ++i) {
        Product product = v->items[i];
        if ((strcmp(category, "") == 0 || strcmp(product.category, category) == 0) &&
            isExpiringInXDays(product.expirationDate, daysUntilExp)) {
            printf("Name: %s, Category: %s, Quantity: %d, Expiration date: %s\n",
                product.name, product.category, product.quantity, product.expirationDate);
        }
    }
}
