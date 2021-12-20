package api

import (
	"sync"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var files = [...]string{
	"title.basics.tsv",
	"title.ratings.tsv",
}

const DB_NAME string = "wsiwn.db"

type WSIWN struct {
	gorm.Model
	Code           string `gorm:"primaryKey"`
	Type           string
	Title          string `gorm:"index"`
	OriginalTitle  string
	StartYear      uint8
	EndYear        uint8
	RuntimeMinutes uint8
	Genres         string
	Rating         float32 `gorm:"type:decimal(2,2)"`
	Votes          uint
}

func DownloadAndExtract(filename string, wg *sync.WaitGroup) {
	defer wg.Done()
	DownloadFile(filename+".gz", "https://datasets.imdbws.com/"+filename+".gz")
	ExtractFile(filename)
}

func SetupDataFiles() {
	var wg sync.WaitGroup
	for _, file := range files {
		wg.Add(1)
		go DownloadAndExtract(file, &wg)
	}
	wg.Wait()
}

func SetupDB() {
	db, err := gorm.Open(sqlite.Open(DB_NAME), &gorm.Config{})
	if err != nil {
		panic("Failed to connect database " + DB_NAME)
	}

	db.AutoMigrate(&WSIWN{})
}
