#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to pointer of the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	*head = prev;
}

/**
 * compare_lists - Compares two linked lists for equality
 * @list1: Pointer to the first list
 * @list2: Pointer to the second list
 * Return: 1 if equal, 0 if not equal
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
		{
			return (0);
		}
		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	prev_slow->next = NULL;

	reverse_list(&slow);

	int is_palindrome = compare_lists(*head, slow);

	reverse_list(&slow);

	if (prev_slow != NULL)
	{
		prev_slow->next = slow;
	}
	else
	{
		*head = slow;
	}

	return (is_palindrome);
}
