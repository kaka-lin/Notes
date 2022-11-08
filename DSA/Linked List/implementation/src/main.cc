#include <iostream>

#include "linked-list.h"
#include "sorted-linked-list-recursion.h"
#include "sorted-linked-list.h"

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
    head = insertion(head, insert_keys[i]);
  }
  print_linked_list(head);

  printf("Insertion: 5\n");
  head = insertion(head, 5);
  print_linked_list(head);

  printf("========== Sorted =========\n");
  SortedLinkedList *sorted_linkde_list = new SortedLinkedList();
  for (i = 0; i < 5; i++) {
    sorted_linkde_list->insertion(insert_keys[i]);
  }
  sorted_linkde_list->printList();

  printf("Insertion: 5\n");
  sorted_linkde_list->insertion(5);
  sorted_linkde_list->printList();

  printf("========== Sorted (Recursion) =========\n");
  ListNode *head2 = NULL;

  // [4, 6, 2, 9, 7]
  // for (i = 0; i < 5; i++) {
  //   scanf("%d", &(array[i]));
  // }
  int insert_keys_2[6] = {4, 6, 2, 9, 7, 5};
  int delete_key_2[2] = {5, 7};
  for (i = 0; i < 6; i++) {
    head2 = insert_linked_list(head2, insert_keys_2[i]);
  }
  print_list(head2);
  printf("Deletion: [5, 7]\n");
  for (i = 0; i < 2; i++) {
    head2 = delete_linked_list(head2, delete_key_2[i]);
  }
  print_list(head2);

  return 0;
}
