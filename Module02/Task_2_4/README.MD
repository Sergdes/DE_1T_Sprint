# Запросы и практика: SQL, join, union и др. 
## Практические задания. SQL.
    1. Чтобы успешно справиться с данным практическим заданием, вам необходимо выполнить как минимум задания 1-4 практики в теме 2.3 "Реляционные базы данных: PostgreSQL", но желательно сделать, конечно же, все.
   2. Теперь мы знакомы с гораздо большим перечнем операторов языка SQL и это дает нам дополнительные возможности для анализа данных. Выполните следующие запросы:

a.     Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.

b.     Попробуйте вывести фамилии сотрудников в алфавитном порядке

c.     Рассчитайте средний стаж для каждого уровня сотрудников

d.     Выведите фамилию сотрудника и название отдела, в котором он работает

e.     Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.

f.      *Выведите название отдела, сотрудники которого получат наибольшую премию по итогам года. Как рассчитать премию можно узнать в последнем задании предыдущей домашней работы

g.    *Проиндексируйте зарплаты сотрудников с учетом коэффициента премии. Для сотрудников с коэффициентом премии больше 1.2 – размер индексации составит 20%, для сотрудников с коэффициентом премии от 1 до 1.2 размер индексации составит 10%. Для всех остальных сотрудников индексация не предусмотрена.

h.    ***По итогам индексации отдел финансов хочет получить следующий отчет: вам необходимо на уровень каждого отдела вывести следующую информацию:

 i.     Название отдела

ii.     Фамилию руководителя

iii.     Количество сотрудников

iv.     Средний стаж

v.     Средний уровень зарплаты

vi.     Количество сотрудников уровня junior

vii.     Количество сотрудников уровня middle

viii.     Количество сотрудников уровня senior

ix.     Количество сотрудников уровня lead

x.     Общий размер оплаты труда всех сотрудников до индексации

xi.     Общий размер оплаты труда всех сотрудников после индексации

xii.     Общее количество оценок А

xiii.     Общее количество оценок B

xiv.     Общее количество оценок C

xv.     Общее количество оценок D

xvi.     Общее количество оценок Е

xvii.     Средний показатель коэффициента премии

xviii.     Общий размер премии.

xix.     Общую сумму зарплат(+ премии) до индексации

xx.     Общую сумму зарплат(+ премии) после индексации(премии не индексируются)

xxi.     Разницу в % между предыдущими двумя суммами(первая/вторая)