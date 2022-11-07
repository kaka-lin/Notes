#include "linked-list.h"

#include <iostream>

ListNode *ListNode::insertion(ListNode *head, int data) {
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

void SortedLinkedList::insertion(int data) {
  ListNode *current = (ListNode *)malloc(sizeof(ListNode));
  ListNode *ptr;
  ListNode *last;

  assert(current != NULL);
  current->data = data;
  if (head == NULL) {
    current->next = NULL;
    head = current;
    return;
  }

  last = NULL;
  ptr = head;
  while (ptr != NULL && ptr->data < data) {
    last = ptr;
    ptr = ptr->next;
  }
  if (last == NULL) {
    current->next = head;
    head = current;
    return;
  } else {
    current->next = last->next;
    last->next = current;
    return;
  }
}

void SortedLinkedList::printList() {
  ListNode *current = head;
  while (current != NULL) {
    std::cout << current->data << " ";
    current = current->next;
  }
  std::cout << std::endl;
}
