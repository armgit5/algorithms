//
//  main.cpp
//  BinTreeLeavesInDoublyLinkedList
//
//  Created by Arm Suwansiri on 6/14/18.
//  Copyright © 2018 Arm Suwansiri. All rights reserved.
//

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *left = NULL;
    Node *right = NULL;
};

// Utility function for printing double linked list.
void printList(Node *head)
{
    while (head)
    {
        printf("%d ", head->data);
        head = head->right;
    }
}

Node* extractLeafList(Node *root, Node **headRef) {
    
    // Base case
    if (root == NULL) return NULL;
    
    // If leaf node
    if (root->left == NULL && root->right == NULL) {
        root->right = *headRef; // Set root right to DLL head
        
        // If head ref, then point to the next left node
        if (*headRef != NULL) (*headRef)->left = root;
        
        // Change head to the current root
        *headRef = root;
        
        return NULL;
    }
    
    // Recursion call left and right tree
    root->right = extractLeafList(root->right, headRef);
    root->left = extractLeafList(root->left, headRef);
    
    return root;
}

int main(int argc, const char * argv[]) {
    
    Node *one, *two, *three, *four, *five, *six, *headRef;
    headRef = NULL;
    one = new Node; one->data = 1;
    two = new Node; two->data = 2;
    three = new Node; three->data = 3;
    four = new Node; four->data = 4;
    five = new Node; five->data = 5;
    six = new Node; six->data = 6;
    
    one->right = three;
    one->left = two;
    three->right = six;
    two->right = five;
    two->left = four;
    
    extractLeafList(one, &headRef);
    
    printf("\nExtracted Double Linked list is:\n");
    printList(headRef);

}
