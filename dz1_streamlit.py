# -*- coding: utf-8 -*-
import streamlit as st


def analiz(stroka):
    # блок определения таблицы переходов
    table_perehod = [['S', '2', 'A'],
                     ['A', '2', 'B'],
                     ['B', '1', 'C'],
                     ['C', 'b', 'S'],
                     ['S', 'b', 'D'],
                     ['D', '2', 'E'],
                     ['E', '1', 'F'],
                     ['F', 'b', 'D'],
                     ['F', '2', 'K'],
                     ['B', '2', 'K'],
                     ['K', '2', 'L'],
                     ['L', '2', 'M'],
                     ['M', '2', 'L']]
    nachaln_simv = 'S'  # начальный символ он у Вас скорее всего 'A'
    kol_perehodov = len(table_perehod)
    length = len(stroka)
    n = 0
    ok = True
    neterm = nachaln_simv
    while ok and (n < length):
        i = 0
        sym = stroka[n]
        print(f"{n} - {sym}")
        n += 1
        ok = False
        while True:
            if (table_perehod[i][0] == neterm) and (table_perehod[i][1] == sym):
                ok = True
                neterm = table_perehod[i][2]
            i += 1
            if not ((not ok) and (i < kol_perehodov)):
                break
    # терминальные символы они у Вас скорее всего 'A'  'E' 'K'
    if ((neterm == 'S') or (neterm == "B") or (neterm == 'F') or (neterm == 'L')) and ok:
        return "# Данная строка принадлежит языку :sunglasses:"
    else:
        return "# Данная строка не принадлежит языку"


if __name__ == "__main__":
    st.markdown('# Дано регулярное выражение (221b)\* (b21)\* (22)*')
    st.markdown('## Введите строку символов:')
    ex = "none"
    ex = st.text_input('', value='', max_chars=None, key='ex' + str(ex), type='default')
    # print(ex)
    rez = analiz(ex)
    # print(rez)
    st.button('Анализ')
    st.markdown(rez)

