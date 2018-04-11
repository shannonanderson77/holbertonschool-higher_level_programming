#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted singly
 * linked list
 * @head: pointer to a singly linked list
 * @number: number to insert
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new_node->n = number;
		new_node = *head;
		return (new_node);
	}
	temp_node = *head;
	while (temp_node->next != NULL)
	{
		temp_node = temp_node->next;
		if ((temp_node->n < number) && (number < temp_node->next->n))
		{
			new_node->n = number;
			new_node->next = temp_node->next->next;
			temp_node->next = new_node;
		}
	}
	return (new_node);
}
