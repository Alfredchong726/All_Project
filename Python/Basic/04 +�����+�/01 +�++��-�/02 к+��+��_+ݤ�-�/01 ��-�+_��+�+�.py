"""
1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
2. 用户用数字选择不同的功能 (input  )
3. 根据功能选择，执行不同的功能( 多分支判断 )
4. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩 、总分 (input 学生信息怎么存储?)
5. 进入或退出时加载或保存数据(文件操作)
"""

str_info = """**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息

0. 退出系统
**************************************************"""

# 读取文件数据


# 循环
while True: # 死循环<因为选择的功能要执行很多次>
    # 1.程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
    print(str_info)
    # 2. 用户用数字选择不同的功能 (input)
    action = input('请输入你要执行的操作:')
    # 3. 根据功能选择，执行不同的功能( 多分支判断 )
    if action == '1':
        print('1. 新建学生信息')
    elif action == '2':
        print('2. 显示全部信息')
    elif action == '3':
        print('3. 查询学生信息')
    elif action == '4':
        print('4. 修改学生信息')
    elif action == '5':
        print('5. 删除学生信息')
    elif action == '0':
        print('0. 退出系统')
        break
    else:
        print('请输入正确的选择!出现未知情况!')

