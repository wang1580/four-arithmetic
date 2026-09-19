import random

# 生成一道四则运算题目
def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*', '/'])
    # 减法保证结果非负，除法保证整除
    if op == '-':
        if a < b:
            a, b = b, a
    elif op == '/':
        a = b * random.randint(1, 10)
    expr = f"{a} {op} {b}"
    return expr, eval(expr)

if __name__ == "__main__":
    print("四则运算练习题")
    count = 3
    for i in range(count):
        q, ans = generate_question()
        print(f"题目{i+1}: {q} = ?")
        user_ans = float(input("你的答案："))
        if abs(user_ans - ans) < 1e-6:
            print("✅ 回答正确")
        else:
            print(f"❌ 错误，正确答案是：{ans}")
