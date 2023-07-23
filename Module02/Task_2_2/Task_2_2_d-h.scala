package org.example
import scala.io.StdIn.readLine

object App {
  def main(args : Array[String]) {
    println("Введите годовой доход:")
    val yearSalalry = readLine().toInt
    println("Введите размер премии в %:")
    val bonus = readLine().toFloat
    println("Компенсация питания:")
    val eatBonus = readLine().toInt
    println("Введите размер пени (введите 0, если штрафов нет):")
    val forfeit = readLine().toInt
    val Salary = ((yearSalalry * bonus / 100 + eatBonus + yearSalalry)/12) * 0.87 - forfeit
    println( s"Зарплата сотрудника в месяц = ${Salary.toInt}" )
    println()


    // 3 d) новый сотрудник и значения макс и мин ЗП
    val newSalary: Double =  Salary.toInt

    val Salaries: List[Double] = List(100, 150, 200, 80, 120, 75)
    val newSalaries: List[Double] = newSalary +: Salaries
    println(s"Сисок ЗП: ${newSalaries}")
    println(s"Самая высокая ЗП: ${newSalaries.max}")
    println(s"Самая низкая ЗП: ${newSalaries.min}")
    println()


    // 3 e) два новых сотрудника и отсортированный по Зп список
    val newSalary_2: List[Double] = List (90, 350)
    val newSalaries_2: List[Double] = newSalary_2 ++ newSalaries
    println(s"Список ЗП по возрастанию: ${newSalaries_2.sorted}")
    println()

    // 3 f) новый сотрудник с окладом 130 тр
    var list_salaries_new = List.empty[Double]
    val NewEmployee: Double = 130
    var step: Int = 0
    var new_salaries_3 = newSalaries_2.sorted
    for (i <- new_salaries_3) {
      if (i <= NewEmployee) {
        step += 1
      }
      list_salaries_new = new_salaries_3.slice(0, step)
      list_salaries_new = list_salaries_new :+ NewEmployee
      list_salaries_new = list_salaries_new ++ new_salaries_3.slice(step, new_salaries_3.length)
    }
    println(s"Список ЗП по возрастанию c новым окладом 130 тысяч: ${list_salaries_new}")
    println()


    // 3 g) вывести номера сотрудников под категорию middle
    var i: Int = 0
    i = 0
    for (n <- list_salaries_new)
      { i += 1
       if ((n >= 120) && (n <= 200))
        println(f"$n middle $i")
      }
    println()


  // 3 h) проиндексировать зарплату на уровень инфляции – 7%
    var IndList: List[Double] = List.empty
    for ( i<- list_salaries_new) {
      var newSal = (i * 1.07).round
      IndList ::= newSal
    }
    println(s"ЗП после индексирования ${IndList.sorted}")


  }

}