import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{IntegerType, StringType, StructType}
import org.apache.spark.sql.functions.{from_json,col}
import org.apache.spark.sql.functions.regexp_replace


object kcpractica {
  //Función Principal de ejecución
  def main(args: Array[String]): Unit = {

    //Crear Sesión Spark
    val spark = SparkSession.builder().appName("kafkaConsumerJSON").master("local[2]").getOrCreate()

    //Crear el "lector en tiempo real que se subscribirá a kafka"
    val dfStream = spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers","localhost:9092")
      .option("subscribe", "topicpractica")
      .option("startingOffsets", "earliest")
      .load()

    //Generar algo legible dese el formato Kafka, lo casteamos primero a STRING
    val resultCast = dfStream.selectExpr( "CAST(value AS STRING)")

    //Generamos el Esquema que tiene nuestro JSON
    val schema = new StructType()
      .add("id", IntegerType)
      .add("first_name", StringType)
      .add("last_name", StringType)
      .add("email", StringType)
      .add("gender", StringType)
      .add("ip_address", StringType)

    //lee los datos casteados, transforma a json con un esquema y genera un alias para operar sobre él
    val personas = resultCast.select( from_json( col("value"), schema).as ("datospersonas"))

    //Seleccionamos todos los datos y reemplazamos en las columnas que hemos seleccionado las palabras indicadas por otros valores
    val datospersonas = personas.select("datospersonas.*")
      .withColumn("email", regexp_replace(col("email"), ".gov", "."))
        .withColumn("first_Name", regexp_replace(col("first_name"), "Jeanette", "-"))
          .withColumn("gender", regexp_replace(col("gender"), "Male", "-"))

    //Mostrar los datos
    println("Los datos son: ")
    datospersonas.writeStream
      .format("console")
      .outputMode("append")
      .start()
      .awaitTermination()
  }
}
