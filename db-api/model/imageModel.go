package model

import (
	"gorm.io/gorm"
)

type Image struct{
	gorm.Model			`json:"-"`
	Id			int		`json:"id"`
	Timestamp	string	`json:"timestamp"`
	Data		[]byte	`json:"data"`		
}

type NewImageData struct{
	Transformed_image		string		`json:"transformed_image" binding:"required"`
}