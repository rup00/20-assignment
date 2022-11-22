def func1():
    print("Inside func1")
    def func2():
        print("Inside func2")
    func2()

func1()