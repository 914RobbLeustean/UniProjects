#include "ui.h"
#include "vector.h"

int main() {

    Vector products;
    vectorInit(&products);

    addOrUpdateProduct(&products, "Milk", "dairy", 10, "2024-01-01");
    addOrUpdateProduct(&products, "Butter", "dairy", 26, "2024-03-18");
    addOrUpdateProduct(&products, "Eggs", "dairy", 20, "2024-03-20");
    addOrUpdateProduct(&products, "Cheese", "dairy", 5, "2024-02-01");
    addOrUpdateProduct(&products, "Chocolate", "sweets", 15, "2024-03-01");
    addOrUpdateProduct(&products, "Candy", "sweets", 25, "2024-03-14");
    addOrUpdateProduct(&products, "Steak", "meat", 10, "2024-04-01");
    addOrUpdateProduct(&products, "Chicken", "meat", 12, "2024-04-15");
    addOrUpdateProduct(&products, "Apples", "fruit", 20, "2024-05-01");
    addOrUpdateProduct(&products, "Bananas", "fruit", 18, "2024-05-15");
    addOrUpdateProduct(&products, "Grapes", "fruit", 30, "2024-06-01");

    handleUserInput(&products);
    vectorFree(&products);
    
    //runAllTests();

    return 0;
}
