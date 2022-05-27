def reverse_list(mylist): #!f #!s;keeptags
    """
    Given a list 'mylist' returns a list consisting of the same elements in reverse order. E.g.
    reverse_list([1,2,3]) should return [3,2,1] (as a list).
    """
    return list(reversed(mylist))

def add(a,b): #!f
    """ Given two numbers `a` and `b` this function should simply return their sum:
    > add(a,b) = a+b """
    return a+b

if __name__ == "__main__":
    # Example usage:
    print(f"Your result of 2 + 2 = {add(2,2)}")
    print(f"Reversing a small list", reverse_list([2,3,5,7])) #!s
