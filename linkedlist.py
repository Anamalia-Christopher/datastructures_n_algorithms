
class SinglyLinkedlist:

    def __init__(self, value, next_node=""):
        self.value = value
        self.link = next_node if next_node else None

    def next_node(self, node):
        self.link = node

    def getNext(self):
        return self.link

    def __repr__(self):
        return str(self.value)

class SinglyLinkedlist_v2(SinglyLinkedlist):

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



if __name__ == "__main__":
    
    a = SinglyLinkedlist_v2(1,2,9,0,4)
    q,w,e,r,t=a()
    print(q.getNext(),w.getNext(),e.getNext(),r.getNext(),t.getNext())
    # a= SinglyLinkedlist(5)
    # b = SinglyLinkedlist(2)
    # a.next_node(b)

    # print(a,b, a.getNext())
