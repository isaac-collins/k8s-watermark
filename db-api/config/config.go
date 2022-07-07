package config

import(
	//"os"
)

var DB_HOST string = "host.docker.internal"//os.Getenv("DB_HOST")
var DB_USER string = "root"//os.Getenv("DB_USER")
var DB_PASSWORD string = "passwordtest"//os.Getenv("DB_PASSWORD")
var DB_PORT string = "4984"