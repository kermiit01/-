def test_function():
    b=4
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
inner_function() # если включить эту функцию в код то пайчарм не может найти такую функцию как inner_function