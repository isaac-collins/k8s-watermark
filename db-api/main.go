package main

import (
	"log"

	"db-api/api"
	"db-api/model"

	
	"github.com/gin-gonic/gin"
)



func main() {

	db, err := model.Database()
	if err != nil {
		log.Println(err)
	}
	db.DB()

	router := gin.Default()

	router.GET("/images", api.GetImages)
	//router.GET("/images<int:ID>", )
	//router.POST ("/images<int:ID>", )

	router.Run("0.0.0.0:8080")
}

