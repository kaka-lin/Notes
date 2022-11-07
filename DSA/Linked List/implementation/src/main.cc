#include <iostream>

#include "linked-list.h"

int main(void) {
  int i;
  int array[5];
  ListNode *head = NULL;

  // [4, 6, 2, 9, 7]
  // for (i = 0; i < 5; i++) {
  //   scanf("%d", &(array[i]));
  // }
  int insert_keys[5] = {4, 6, 2, 9, 7};
  for (i = 0; i < 5; i++) {
    head = head->insertion(head, insert_keys[i]);
  }
  print_linked_list(head);

  printf("Add: 5\n");
  head = head->insertion(head, 5);
  print_linked_list(head);

  printf("========== Sorted =========\n");
  SortedLinkedList *sorted_linkde_list = new SortedLinkedList();
  for (i = 0; i < 5; i++) {
    sorted_linkde_list->insertion(insert_keys[i]);
  }
  sorted_linkde_list->printList();

  printf("Add: 5\n");
  sorted_linkde_list->insertion(5);
  sorted_linkde_list->printList();

  return 0;
}
