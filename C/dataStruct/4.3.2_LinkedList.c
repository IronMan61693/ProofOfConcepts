#include <stdlib.h>
#include <stdio.h>

struct node
  {
    int intInfo;
	  struct node* nextNode;
  };

struct node* last = NULL;

void insertAtFront(int intData)
  {
    struct node* temp;
	  temp = (struct node*)malloc(sizeof(struct node));

  	// If empty
  	if (last == NULL)
  	  {
  	    temp->intInfo = intData;
    		temp->nextNode = temp;
    		last = temp;
  	  }
  	else
  	  {
  	    temp->intInfo = intData;
    		temp->nextNode = last->nextNode;
    		last->nextNode = temp;
  	  }
  }

void insertAtEnd (int intData)
  {
    struct node* temp;
	  temp = (struct node*)malloc(sizeof(struct node));

  	// If empty
  	if (last == NULL)
  	  {
  	    temp->intInfo = intData;
    		temp->nextNode = temp;
    		last = temp;
  	  }
  	else
  	  {
  	    temp->intInfo = intData;
    		last->nextNode = temp;
    		last = temp;
  	  }
  }

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

void printListData()
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
    		do
    		  {
    		    printf("Data of current node %d \n", temp->intInfo);
      			temp = temp->nextNode;
    		  } while(temp != last->nextNode);
  	  }
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
