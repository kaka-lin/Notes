#ifndef SORTED_LINKED_LIST_H
#define SORTED_LINKED_LIST_H

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>

#include "linked-list.h"

// typedef struct listnode {
//   int data;
//   struct listnode *next;
// } ListNode;

class SortedLinkedList {
 public:
  SortedLinkedList() : head(NULL){};

  // Insertionthis
  void insertion(int data);

  // Show
  void printList();

 private:
  ListNode *head;
};

#endif  // SORTED_LINKED_LIST_H
