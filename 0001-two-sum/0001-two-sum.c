#include <stdio.h>
#include <stdlib.h>

// Hash map structure
typedef struct {
    int key;   // number from nums
    int value; // index
} HashItem;

#define TABLE_SIZE 10007  // A prime number for hash table size

int hash(int key) {
    if (key < 0) key = -key;
    return key % TABLE_SIZE;
}

void insert(HashItem *table, int key, int value) {
    int index = hash(key);
    while (table[index].key != 0 || table[index].value != -1) {
        index = (index + 1) % TABLE_SIZE;
    }
    table[index].key = key;
    table[index].value = value;
}

int search(HashItem *table, int key) {
    int index = hash(key);
    while (table[index].value != -1) {
        if (table[index].key == key) return table[index].value;
        index = (index + 1) % TABLE_SIZE;
    }
    return -1;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));

    HashItem *table = (HashItem*)malloc(TABLE_SIZE * sizeof(HashItem));
    for (int i = 0; i < TABLE_SIZE; i++) {
        table[i].key = 0;
        table[i].value = -1;
    }

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int foundIndex = search(table, complement);
        if (foundIndex != -1) {
            result[0] = foundIndex;
            result[1] = i;
            free(table);
            return result;
        }
        insert(table, nums[i], i);
    }

    free(table);
    return NULL;
}
