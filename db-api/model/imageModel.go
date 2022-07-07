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