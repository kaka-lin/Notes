#include "sorted-linked-list-recursion.h"

#include <iostream>

ListNode *insert_linked_list(ListNode *head, int data) {
  ListNode *current = (ListNode *)malloc(sizeof(ListNode));
  assert(current != NULL);
  current->data = data;
  if (head == NULL || data < head->data) {
    current->next = head;
    return (current);
  }
  head->next = insert_linked_list(head->next, data);
  return (head);
}

ListNode *delete_linked_list(ListNode *head, int data) {
  ListNode *temp;
  if (head == NULL) return NULL;
  if (data == head->data) {
    temp = head->next;
    free(head);
    return (temp);
  }
  head->next = delete_linked_list(head->next, data);
  return (head);
}

void print_list(ListNode *head) {
  if (head == NULL) {
    printf("\n");
    return;
  }
  printf("%d ", head->data);
  print_list(head->next);
}
