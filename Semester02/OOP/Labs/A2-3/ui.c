#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ui.h"
#include "controller.h"


//Implementation of printMenu and handleUserInput that interacts with the user

void printMenu() {
    /*Prints the interactive menu for the user, showing available actions*/

    printf("\nIntelligent Refrigerator Management System\n");
    printf("1. Add/Update Product\n");
    printf("2. Delete Product\n");
    printf("3. Filter & Display Products\n");
    printf("4. Display all products of a given category close to expiration\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

void handleUserInput(Vector* products) {
    int choice;
    char name[MAX_NAME], category[MAX_NAME], expirationDate[MAX_NAME];
    int quantity;

    do {
        printMenu();
        scanf("%d", &choice);
        getchar(); // Consume newline

        switch (choice) {
        case 1:
            printf("Enter product name: ");
            fgets(name, MAX_NAME, stdin);
            name[strcspn(name, "\n")] = 0; // Remove newline

            printf("Enter category (dairy, sweets, meat, fruit): ");
            fgets(category, MAX_NAME, stdin);
            category[strcspn(category, "\n")] = 0; // Remove newline

            printf("Enter quantity: ");
            scanf("%d", &quantity);
            getchar(); // Consume newline

            printf("Enter expiration date (YYYY-MM-DD): ");
            fgets(expirationDate, MAX_NAME, stdin);
            expirationDate[strcspn(expirationDate, "\n")] = 0; // Remove newline

            addOrUpdateProduct(products, name, category, quantity, expirationDate);
            printf("Product added/updated successfully.\n");
            break;

        case 2:
            printf("Enter product name to delete: ");
            fgets(name, MAX_NAME, stdin);
            name[strcspn(name, "\n")] = 0;

            printf("Enter category: ");
            fgets(category, MAX_NAME, stdin);
            category[strcspn(category, "\n")] = 0;

            deleteProduct(products, name, category);
            printf("Product deleted successfully.\n");
            break;

        case 3: {
            int filterType = 0;
            char searchString[MAX_NAME] = { 0 };
            int quantityThreshold = 0;
            int sortOrder;

            printf("Filter by: 1- Search string, 2- Quantity threshold: ");
            scanf("%d", &filterType);
            getchar(); // Consume newline

            if (filterType == 1) {
                printf("Enter the search string: ");
                fgets(searchString, MAX_NAME, stdin);
                searchString[strcspn(searchString, "\n")] = '\0'; // Remove newline
            }
            else if (filterType == 2) {
                printf("Enter the maximum quantity threshold: ");
                scanf("%d", &quantityThreshold);
                getchar(); // Consume newline
            }
            else {
                printf("Invalid filter type.\n");
                break;
            }

            printf("Choose sort order: 1- Ascending, 2- Descending: ");
            scanf("%d", &sortOrder);
            getchar(); // Consume newline

            int (*compareFunc)(const void*, const void*) = NULL;
            if (sortOrder == 1) {
                compareFunc = compareByQuantityAsc; // Assumes this function is defined elsewhere
            }
            else if (sortOrder == 2) {
                compareFunc = compareByQuantityDesc; // Assumes this function is defined elsewhere
            }
            else {
                printf("Invalid sort order.\n");
                break;
            }

            displayProductsFiltered(products, searchString, quantityThreshold, filterType, compareFunc);
            break;
        }


        case 4:
            printf("Enter the category you wish to display: ");
            fgets(category, MAX_NAME, stdin);
            category[strcspn(category, "\n")] = 0;

            int days;
            printf("Enter the number of days until expiration: ");
            if (scanf("%d", &days) != 1) {
                printf("Invalid input for the number of days.\n");
                break;
            }
            getchar(); // Consume the leftover newline character after scanf

            displayProductsByCategoryAndExpiration(products, category, days);
            break;


        case 5:
            printf("Exiting program...\n");
            return;

        default:
            printf("Invalid choice. Please enter a number between 1 and 6.\n");
      
        }
    } while (1);
}
