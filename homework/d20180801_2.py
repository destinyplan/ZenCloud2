while True:
    oprt = input("请选择需要执行的选项:")
    print("你选择了选项:",oprt)
    if oprt == "1":
        print("吃饭")
    elif oprt == "2":
        print("睡觉")
    elif oprt == "3":
        print("打豆豆")
    elif oprt == "exit":
        print("正在退出")
    else:
        print("输入错误，请重新输入")
print("End")
