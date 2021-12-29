package api

import (
	"encoding/csv"
	"io"
	"log"
	"os"
	"strconv"
	"sync"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"gorm.io/gorm/clause"
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
	StartYear      uint
	EndYear        uint
	RuntimeMinutes uint
	Genres         string
	Rating         float32 `gorm:"type:decimal(2,2)"`
	Votes          uint
}

func DownloadAndExtract(filename string, wg *sync.WaitGroup) {
	defer wg.Done()
	DownloadFile(filename+".gz", "https://datasets.imdbws.com/"+filename+".gz")
	ExtractFile(filename)
	logger(false, false, "File downloaded:", filename)
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

	UpdateTitles(db)
	UpdateRatings(db)
}

func UpdateTitles(db *gorm.DB) {
	file, err := os.Open(files[0])
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	csvReader := csv.NewReader(file)
	csvReader.Comma = '\t'
	csvReader.LazyQuotes = true
	csvReader.TrimLeadingSpace = true
	var rows_count int64 = 0

	for {
		line, err := csvReader.Read()
		if err == io.EOF {
			break
		} else if err != nil {
			logger(true, true, "Skipping row after:", rows_count, "\nError:", err)
		} else if line[0] == "tconst" {
			continue
		}

		res := db.Clauses(clause.OnConflict{UpdateAll: true}).Create(&WSIWN{
			Code:           line[0],
			Type:           line[1],
			Title:          line[2],
			OriginalTitle:  line[3],
			StartYear:      convertUint(line[5]),
			EndYear:        convertUint(line[6]),
			RuntimeMinutes: convertUint(line[7]),
			Genres:         line[8],
		})
		rows_count += res.RowsAffected
	}

	logger(false, false, "Titles updated:", rows_count)
}

func UpdateRatings(db *gorm.DB) {
	file, err := os.Open(files[1])
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	csvReader := csv.NewReader(file)
	csvReader.Comma = '\t'
	csvReader.LazyQuotes = true
	csvReader.TrimLeadingSpace = true
	var rows_count int64 = 0

	for {
		line, err := csvReader.Read()
		if err == io.EOF {
			break
		} else if err != nil {
			logger(true, true, "Skipping row after:", rows_count, "\nError:", err)
		} else if line[0] == "tconst" {
			continue
		}

		rating, err := strconv.ParseFloat(line[1], 32)
		if err != nil {
			logger(true, true, "Invalid rating after row:", rows_count, "\nError:", err)
			rating = 0
		}

		res := db.Clauses(clause.OnConflict{UpdateAll: true}).Create(&WSIWN{
			Code:   line[0],
			Rating: float32(rating),
			Votes:  convertUint(line[2]),
		})
		rows_count += res.RowsAffected
	}

	logger(false, false, "Ratings updated:", rows_count)
}
