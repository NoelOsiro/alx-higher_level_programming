#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1); 
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
	}
	prev_slow->next = NULL;
	listint_t *prev = NULL;
	listint_t *current = second_half;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	second_half = prev;
	listint_t *first_half = *head;

	while (first_half != NULL && second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	prev_slow->next = second_half;
	prev = NULL;
	current = prev_slow;
	while (current->next != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	current->next = prev;

	return (is_palindrome);
}
