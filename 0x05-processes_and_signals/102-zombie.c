#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite number of loops
 * Return: 0 if successful
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates zombies
 * Return: 0 if successful
 */
int main(void)
{
	pid_t child_pid = 0;
	int i;

	child_pid = fork();

	for (i = 0; i < 5; i++)
	{
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %i\n", child_pid);
		}
		else
		{
			exit(EXIT_SUCCESS);
		}
	}
	infinite_while();

	return (0);
}
