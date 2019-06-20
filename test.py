from linked_list.linked_list import LL


if __name__ == "__main__":
    obj = LL()
    obj.insert_first(1)
    obj.insert_first(2)
    obj.insert_first(3)
    print('-'*60)
    print('LENGTH: {}'.format(obj.get_length()))

    print('-'*60)
    print('LIST CONTENTS')
    print('-'*60)
    obj.traversal()

    print('-'*60)
    print('SEARCH OPERATION')
    print('-'*60)
    print(obj.search(3))
    print(obj.search(-1))

    print('-'*60)
    print('DELETION OPERATION')
    print('-'*60)
    print(obj.delete(2))
    print(obj.delete(-1))

    print('\n\nafter deletion')
    obj.traversal()