package api

import (
	"net/http"
	"log"
	"db-api/model"
	"github.com/gin-gonic/gin"
	"time"
	"encoding/base64"
)

func GetImages(c *gin.Context) {

	var images []model.Image


	db, err := model.Database()
	if err != nil {
		log.Println(err)
	}
	if err := db.Find(&images).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, images)
}

func PostImage(c *gin.Context) {

	var inputdata model.NewImageData


	db, err := model.Database()
	if err != nil {
		log.Println(err)
	}

	err = c.ShouldBindJSON(&inputdata)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
	}

	imageBytes, err := base64.StdEncoding.DecodeString(inputdata.Transformed_image)
    if err != nil {
		log.Println(err)
    }


	image := model.Image{Timestamp: time.Now().String(), Data: imageBytes}
	db.Create(&image)
	c.JSON(http.StatusOK, image)
}

func GetImage(c *gin.Context) {

	var image model.Image

	db, err := model.Database()
	if err != nil {
		log.Println(err)
	}

	if err := db.Where("id = ?", c.Param("id")).First(&image).Error; err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Not Found"})
		return
	}
	
	c.JSON(http.StatusOK, image)
}