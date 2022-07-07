package api

import (
	"net/http"
	"log"
	"db-api/model"
	"github.com/gin-gonic/gin"
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