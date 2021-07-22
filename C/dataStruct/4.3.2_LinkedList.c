#include <stdlib.h>
#include <stdio.h>

// Note to self, increase size of data by 1, insert at from char for data type
// To be referenced when calling function for print
struct node
  {
    // Using a pointer to allow for storing any data type
    void *data;
	  struct node* nextNode;
  };

// Initializing as a global the last node (used for tracking the list)
struct node* last = NULL;


void insertAtFront(void *new_data, size_t new_data_size)
// As the name suggests, expects pointer to data and the data's size
  {
    struct node* temp = (struct node*)malloc(sizeof(struct node));

    temp->data = malloc(data_size);
  	// If empty
  	if (last == NULL)
  	  {
    		temp->nextNode = temp;
    		last = temp;
  	  }
  	else
  	  {
    		temp->nextNode = last->nextNode;
    		last->nextNode = temp;
  	  }
    // Now copying data into allocated memory
    int i;
    for (i=0; i<data_size; i++)
     {
       // address allocated plus i spots assuming char is a size of 1, one char at a time
       *(char *)(temp->data + i) = *(char *)(new_data + i)
     }
  }

void insertAtEnd (void *new_data, size_t new_data_size)
// As the name suggests, expects pointer to data and the data's size
  {
    struct node* temp = (struct node*)malloc(sizeof(struct node));

    temp->data = malloc(data_size);
  	// If empty
  	if (last == NULL)
  	  {
    		temp->nextNode = temp;
    		last = temp;
  	  }
  	else
  	  {
    		temp->nextNode = last->nextNode;
    		last->nextNode = temp;
        // Just need to move last such that it is now temp
        last = temp;
  	  }
    // Now copying data into allocated memory
    int i;
    for (i=0; i<data_size; i++)
     {
       // address allocated plus i spots assuming char is a size of 1, one char at a time
       *(char *)(temp->data + i) = *(char *)(new_data + i)
     }
  }

/* Will fix shortly
void insertAtLocation (int location, int intData)
  {
    struct node* temp;
  	struct node* walkerNode;
  	int indexCount =1;
	   temp = (struct node*)malloc(sizeof(struct node));
	if (location == 0)
	  {
	    printf("insertAtFront in location");
		    insertAtFront(intData);
	  }
	else if (last == NULL)
	  {
	    printf("There are no nodes to insert at location, instantiating at 0");
  		temp->intInfo = intData;
  		temp->nextNode = temp;
  		last = temp;
	  }
	else
	  {
	    walkerNode = last->nextNode;
		  while(walkerNode != last & indexCount < location)
		    {
		      indexCount += 1;
			    walkerNode = walkerNode->nextNode;
		    }
		  if (walkerNode == last)
		    {
		      printf("Looks like your request is the end or beyond the end of the list, adding to end");
			    insertAtEnd(intData);
		    }
	  	else
		    {
		      temp->intInfo = intData;
			    temp->nextNode = walkerNode->nextNode;
			    walkerNode->nextNode = temp;
		    }
	  }
  }
*/

void removeAtLocation(int location)
  {
    struct node* deleteNode;
  	struct node* rearNode;
  	int index = 0;
  	if (last == NULL)
	    {
	      printf("The list is empty, nothing to remove");
	    }
	  else
	    {
	      deleteNode = last->nextNode;
		    rearNode = last->nextNode;
		if (location == 0)
		  {
		    last->nextNode = rearNode->nextNode;
		  	rearNode = last;
		  	if (last == deleteNode)
			    {
			      last = NULL;
			    }
			  free(deleteNode);
		  }

		while (rearNode != last) // && index != location
		  {
		    index += 1;
  			deleteNode = rearNode->nextNode;
  			if (index == location)
			    {
			      rearNode->nextNode = deleteNode->nextNode;
				    if (deleteNode == last)
				      {
				        last = rearNode;
				      }
				    free(deleteNode);
			    }
		  }
	  }
  }

void printListData(void (*fptr)(void *))
// This let's us access functions for printing whatever the data type is
  {
    printf("Print Check\n");
  	if (last == NULL)
  	  {
  	    printf("The list is currently empty \n");
  	  }
  	else
  	  {
  	    printf("Start print \n");
    		struct node* temp;
    		temp = last->nextNode;
    		while (temp != NULL)
    		  {
    		    printf("Data of current node ");
            (*fptr)(temp->data);
            printf("\n");
      			temp = temp->nextNode;
    		  }
  	  }
  }

void printInt(void *n)
  {
    printf("%d", *(int *)n);
  }

void printFloat(void *f)
  {
    printf("%f", *(float *)f);
  }

void printFloat(void *f)
  {
    printf("%f", *(float *)f);
  }

void cleanList()
  {
    while (last != NULL)
  	  {
  	    printf("clean node check\n");
    		removeAtLocation(0);
    		printListData();
  	  }
  }

int main()
  {
    printListData();
  	insertAtFront(2);
  	insertAtEnd(4);
  	// insertAtFront(1);
  	// insertAtEnd(5);
  	// printListData();
  	// insertAtLocation(2,3);
  	printListData();
  	removeAtLocation(1);
  	printListData();
  	cleanList();
  	printListData();
  	removeAtLocation(0);
  	printListData();

  	return 0;
  }
