def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return [i for i in iterable if function(i)]

print(filter.__doc__)
print(ft_filter.__doc__)