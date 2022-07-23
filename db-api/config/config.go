package config

import(
	"os"
)

var DB_HOST string 		= os.Getenv("DB_HOST")
var DB_USER string 		= os.Getenv("DB_USER")
var DB_PASSWORD string 	= os.Getenv("DB_PASSWORD")
var DB_PORT string 		= os.Getenv("DB_PORT")