#ifndef SORTED_LINKED_LIST_RECURSION_H
#define SORTED_LINKED_LIST_RECURSION_H

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include <iostream>

#include "linked-list.h"

// typedef struct listnode {
//   int data;
//   struct listnode *next;
// } ListNode;

// Insertion
ListNode *insert_linked_list(ListNode *head, int data);

// Deletion
ListNode *delete_linked_list(ListNode *head, int data);

void print_list(ListNode *head);

#endif  // SORTED_LINKED_LIST_RECURSION_H
