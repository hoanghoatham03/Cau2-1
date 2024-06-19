import streamlit as st

st.title('Tính toán số học')

number1 = st.number_input('Nhập số thứ nhất', value=0.0)
number2 = st.number_input('Nhập số thứ hai', value=0.0)

operation = st.selectbox('Chọn phép tính', ['Tổng', 'Hiệu', 'Tích', 'Thương'])

result = None
if st.button('Tính toán'):
    if operation == 'Tổng':
        result = number1 + number2
    elif operation == 'Hiệu':
        result = number1 - number2
    elif operation == 'Tích':
        result = number1 * number2
    elif operation == 'Thương':
        if number2 != 0:
            result = number1 / number2
        else:
            result = 'Không thể chia cho 0'

if result is not None:
    st.success(f'Kết quả của phép tính {operation} là: {result}')

# Link web: https://21522120-cau2-1.streamlit.app/
