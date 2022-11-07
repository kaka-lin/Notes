#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>

struct ListNode {
  int data;
  struct ListNode *next;

  // Insertion
  ListNode *insertion(ListNode *head, int data);
};

void print_linked_list(ListNode *head);

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

#endif  // LINKED_LIST_H
