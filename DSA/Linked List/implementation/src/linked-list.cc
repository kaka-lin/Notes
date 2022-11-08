#include "linked-list.h"

#include <iostream>

ListNode *insertion(ListNode *head, int data) {
  ListNode *current = (ListNode *)malloc(sizeof(ListNode));
  assert(current != NULL);
  current->data = data;
  current->next = head;
  head = current;
  return (head);
}

void print_linked_list(ListNode *head) {
  for (; head != NULL; head = head->next) {
    printf("%d ", head->data);
  }
  printf("\n");
}
