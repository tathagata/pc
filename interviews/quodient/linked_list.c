#include <stdio.h>
#include <malloc.h>
typedef struct Node {
	int value;
	struct Node *next;
}node;
node *head;

node * create_node(int value){
	node *new=(node*)malloc(sizeof(node));
	new->value = value;
	new->next = NULL;
	return new;	
}

void print_list(node *n){
	node *temp = (node *)malloc(sizeof(node));
	temp = n;
	while(temp!=NULL){
		printf("%d ",temp->value);
		temp=temp->next;
	}
	printf("\n");
}


void reverse_list(node *n){
	if (n==NULL)
		return;
	node *temp, *prev, *a;
	temp = n;
	prev = NULL;
	while(temp->next!=NULL){
		a = temp->next;	
		temp->next=prev;
		prev = temp;
		temp=a;
	}
	temp->next=prev;
	return;
}



int main(int argc, const char *argv[]){
	node *temp = (node *)malloc(sizeof(node));
	head = (node *)malloc(sizeof(node));
	head=create_node(0);
	temp = head;
		
	int i;
	for (i=1;i<10;i++){
		temp->next = create_node(i);
		temp=temp->next;
	}
	
	reverse_list(head);
	
	print_list(temp);
	return 0;
}




