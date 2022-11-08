#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>

typedef struct listnode {
  int data;
  struct listnode *next;
} ListNode;

// Insertion
ListNode *insertion(ListNode *head, int data);

void print_linked_list(ListNode *head);

#endif  // LINKED_LIST_H
