
class SinglyLinkedlist:

    def __init__(self, value, next_node=""):
        self.value = value
        self.link = next_node if next_node else None

    def next_node(self, node):
        self.link = node

    def get_next(self):
        return self.link

    def set_value(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

class SinglyLinkedlist_v2:

    listing = []
    def __init__(self, *args, **kwargs):

        self.args = list(args)
        self.args.reverse()

    def __call__(self): 
        prev = None
        for i in self.args:

            self.listing.append(self.linking(i, prev))
            prev = self.linking(i, prev)
        self.listing.reverse()
        return self.listing

    def linking(self, value, next_node):
        return SinglyLinkedlist(value, next_node)

    def __delattr__(self, name):
        return super().__delattr__(name)

class DoublyLinkedlist:

    def __init__(self, value, _prev=None, _next=None):
        self.value = value
        self.prev = _prev
        self.next = _next

    def next_node(self, node):
        self.next = node

    def prev_node(self, node):
        self.prev = node

    def linked_nodes(self, prev, next):
        self.prev_node(prev)
        self.next_node(next)

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_value(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

     

    
class DoublyLinkedlist_v2:
    
    def __init__(self, *args):
        self.args = args
        self.listing = []
    
    def __call__(self):
        length = len(self.args)
        for i in range(length):
            if i == 0:
                self.listing.append(self.linking(self.args[i], None, None))
                continue
            self.listing.append(self.linking(self.args[i], self.listing[-1], None))
            self.listing[-2].next_node(self.listing[-1])

        return self.listing
    
    def linking(self, value, _prev, _next):
        return DoublyLinkedlist(value, _prev, _next)

    def unlinking(self, node):
        i = self.listing.index(node)

        self.listing[i-1].next_node(self.listing[i+1])
        self.listing[i+1].prev_node(self.listing[i-1])
        if i==0:
            self.listing[i+1].prev_node(None)
        if i==len(self.listing):
            self.listing[i-1].next_node(None)
        self.listing.pop(i)

    def __delitem__(self, node):
       
        self.unlinking(node)


        




if __name__ == "__main__":

    v2 = DoublyLinkedlist_v2(2,1,3,5,3,5,6)
    a,b,c,d,e,f,g = v2()

    print( a.get_prev(), a, a.get_next())
    print( g.get_prev(), g,g.get_next())
    print( d.get_prev(), d,d.get_next())


    del v2[0] # for unlinking the variable from the linkedlist 
    del c # for deleting the variable from memmory 

    
    print(d.get_prev(), d,d.get_next())






    # a = DoublyLinkedlist(34)
    
    # b = DoublyLinkedlist(12, _prev=a)
    # a.next_node(b)
    # c = DoublyLinkedlist(190, _prev=b)
    # b.next_node(c)

    # d = DoublyLinkedlist(-43, _prev=c)
    # c.next_node(d)

    # e = DoublyLinkedlist(1243, _prev=d)
    # d.next_node(e)
    # # print(d.get_prev(), b.get_next())

    # print(d.get_prev(), b.get_next(),2345678)
    
    
    


    # a = SinglyLinkedlist_v2(1,2,9,0,4)
    # q,w,e,r,t=a()
    # print(q.get_next(),w.get_next(),e.get_next(),r.get_next(),t.get_next())
    # a= SinglyLinkedlist(5)
    # b = SinglyLinkedlist(2)
    # a.next_node(b)

    # print(a,b, a.get_next())
