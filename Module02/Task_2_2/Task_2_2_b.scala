package org.example

/**
 * @author ${user.name}
 */
object App {
  
  def main(args : Array[String]) {
    var starVarString = "Hello, Scala!"
    println(starVarString.reverse)
    println(starVarString.toLowerCase)
    println(starVarString.init)
    println(starVarString + " and goodbye python!")

  }

}