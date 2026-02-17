import streamlit as st
import math

st.set_page_config(page_title="高级科学计算器", page_icon="🧮")

st.title("🧮 高级科学计算器")

# 初始化历史记录
if "history" not in st.session_state:
    st.session_state.history = []

# 角度模式
angle_mode = st.radio("角度模式", ["角度 (Degree)", "弧度 (Radian)"])

# 输入表达式
expression = st.text_input("请输入数学表达式（例如: sin(30) + 2^3）")

def safe_eval(expr):
    try:
        # 替换符号
        expr = expr.replace("^", "**")

        # 允许的数学函数
        allowed_names = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial,
            "abs": abs,
            "pow": pow
        }

        # 角度转弧度
        if angle_mode == "角度 (Degree)":
            allowed_names["sin"] = lambda x: math.sin(math.radians(x))
            allowed_names["cos"] = lambda x: math.cos(math.radians(x))
            allowed_names["tan"] = lambda x: math.tan(math.radians(x))

        return eval(expr, {"__builtins__": {}}, allowed_names)

    except Exception as e:
        return f"错误: {e}"

if st.button("计算"):
    if expression:
        result = safe_eval(expression)
        st.success(f"结果: {result}")
        st.session_state.history.append(f"{expression} = {result}")

# 显示历史
st.subheader("📜 计算历史")

for item in reversed(st.session_state.history):
    st.write(item)

if st.button("清空历史"):
    st.session_state.history = []
