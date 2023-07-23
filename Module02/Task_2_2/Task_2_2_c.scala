package org.example
import scala.io.StdIn.readLine

object App {
  
  def main(args : Array[String]) {
    println( "Введите годовой доход:" )
    val yearSalalry = readLine().toInt
    println( "Введите размер премии:" )
    val bonus = readLine().toFloat
    println( "Компенсация питания:" )
    val eatBonus = readLine().toInt
    val Sum = ((yearSalalry * bonus/100 + eatBonus + yearSalalry)/12) * 0.87
    println(Sum)
  }

}