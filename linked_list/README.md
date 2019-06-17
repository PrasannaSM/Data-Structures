# LINKED LIST:

Similar to array but each element is an object
element/node consists of

Data
Reference to next node

####
    --> Accessing time of an element    : O(n)
    --> Search time of an element       : O(n)
    --> Insertion of an Element         : O(1) [If we are at the position where we have to insert an element]
    --> Deletion of an Element          : O(1) [If we know address of node previous the node to be deleted]


#### Advantage of linked list over arrays is that it is scalable.
#### Disadvantage is random access is not allowed as there are no indices like in arrays. We have to traverse the list taking O(i) time.

# TYPES :

#### SINGLY LINKED LIST

#### DOUBLY LINKED LIST

#### XOR DOUBLY LINKED LIST
    --> Memory efficient doubly linked list where only one space is used to store both prev and next addresses.
    --> This memory efficient Doubly Linked List is called XOR Linked List or Memory Efficient as the list uses bitwise XOR operation to save space for one address.
    --> In the XOR linked list, instead of storing actual memory addresses, every node stores the XOR of addresses of previous and next nodes.
    --> Traversal
            ->  Can be done in both forward and backward direction.
	        ->  While traversing the list we need to remember the address of the previously accessed node in order to calculate the next node’s address

#### CIRCULAR LINKED LIST
    --> There is no NULL at the end

# LINKED LIST VS ARRAYS
    --> The size of the arrays is fixed, Linked Lists are Dynamic in size.
    --> Inserting and deleting a new element in an array of elements is expensive, Whereas both insertion and deletion can easily be done in Linked Lists.
    --> Random access is not allowed in Linked List.
    --> Extra memory space for a pointer is required with each element of the Linked list.
    --> Arrays have better cache locality that can make a pretty big difference in performance. In particular, arrays are contiguous memory blocks, so large chunks of them will be loaded into the cache upon first access. This makes it comparatively quick to access future elements of the array.
    --> Linked lists on the other hand aren't necessarily in contiguous blocks of memory, and could lead to more cache misses, which increases the time it takes to access them.