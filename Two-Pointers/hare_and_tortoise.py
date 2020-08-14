


hare = head
tortoise = head
it = 0

while hare != None:
	hare = hare.next
	if it % 2 == 1:
		continue
	tortoise = tortoise.next