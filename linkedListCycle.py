def has_cycle(head):
    if head.next == None:
        # print('head.next = None')
        # print(head, head.next)
        return False
    store = {head}
    #print('head.next: ', head.next, '---------------')
    next = head.next
    # print(head, next, head.next)
    while next != None:
        # print('while')
        if (next in store):
            # print('next in store')
            # print('next: ', next)
            # print('head: ', head)
            # print('store: ', store)
            return True
        store.add(next)
        next = next.next
    return False
