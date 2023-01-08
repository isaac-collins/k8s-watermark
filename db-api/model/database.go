package model

import (
	"db-api/config"
	"fmt"
	"time"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

func Database() (*gorm.DB, error) {
	DB_CONNECTION := fmt.Sprintf("%s:%s@tcp(%s:%s)/images?parseTime=true", config.DB_USER, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT)
	var err error
	retries := 5
	var db *gorm.DB
	db, err = gorm.Open(mysql.Open(DB_CONNECTION), &gorm.Config{})
	for err != nil {
		db, err = gorm.Open(mysql.Open(DB_CONNECTION), &gorm.Config{})
		time.Sleep(time.Second)
		retries--
		if retries == 1 {
			panic(err)
		}
	}

	return db, err
}
