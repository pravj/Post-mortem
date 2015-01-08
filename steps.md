* Using Google BigQuery download csv data for repositories with stars >= 500
* Remove corrupted lines in data
  * The Vim Game `:g/https\:\/\/github\.com\/\//d`
  * removes 894 corrupted lines; 9068 -> 8174
