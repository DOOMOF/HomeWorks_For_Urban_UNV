def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
#inner_function() данную функцию нельзя вызвать, так как она находиться в области видимости test_function() 
