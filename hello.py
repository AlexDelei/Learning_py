def get_hello_message():
    text = "pineappple"
    x = text.upper()

    print(x)

    a, b, c = "yoghurt", "soda", "cake"
    f, g, h = 100, 180, 50
    items = "The prices of : {2} is {4} shillings, {1} for {5} shillings and {0} for {3} shillings only"
    result = items.format(a, b, c, f, g, h)
    return result