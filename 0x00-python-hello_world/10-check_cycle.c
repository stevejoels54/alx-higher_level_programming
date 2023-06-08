#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: Pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * Description: Floyd's cycle-finding algorithm
 */

int check_cycle(listint_t *list)
{
	listint_t *one_step, *two_step;

	one_step = list;
	two_step = list;
	while (one_step && two_step && two_step->next)
	{
		one_step = one_step->next;
		two_step = two_step->next->next;
		if (one_step == two_step)
			return (1);
	}

	return (0);
}
