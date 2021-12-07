package api

import "sync"

var files = [...]string{
	"title.basics.tsv",
	"title.ratings.tsv",
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
