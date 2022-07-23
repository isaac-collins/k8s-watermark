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
	db.AutoMigrate(&model.Image{})

	router := gin.Default()

	router.GET("/images", api.GetImages)
	router.POST("/images", api.PostImage)
	router.GET("/images/:id", api.GetImage)

	router.Run("0.0.0.0:5000")
}

