package model

import (
	"fmt"
	"db-api/config"
	"gorm.io/gorm"
	"gorm.io/driver/mysql"
)

func Database() (*gorm.DB, error) {
	DB_CONNECTION := fmt.Sprintf("%s:%s@tcp(%s:%s)/images", config.DB_USER, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT)
	
	db, err := gorm.Open(mysql.Open(DB_CONNECTION), &gorm.Config{})
	if err != nil {
		fmt.Println("Error opening db connection ", err)
	} else {
		fmt.Println("Connected to DB")
	}

	return db, err

}