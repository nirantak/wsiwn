package api

import (
	"compress/gzip"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/spf13/viper"
)

func logger(verbose bool, err bool, msg ...interface{}) {
	var op *os.File = os.Stdout
	if err {
		op = os.Stderr
	}

	if verbose && !viper.GetBool("verbose") {
	} else {
		fmt.Fprintln(op, msg...)
	}
}

func convertUint(val string) uint {
	res, err := strconv.ParseUint(val, 10, 32)
	if err != nil {
		return 0
	}
	return uint(res)
}

func DownloadFile(filename string, url string) {
	out, err := os.Create("./" + filename)
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	_, err = io.Copy(out, resp.Body)
	if err != nil {
		log.Fatal(err)
	}

}

func ExtractFile(filename string) {
	file, err := os.Open("./" + filename + ".gz")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	out, err := os.Create("./" + filename)
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	data, err := gzip.NewReader(file)
	if err != nil {
		log.Fatal(err)
	}
	defer data.Close()

	_, err = io.Copy(out, data)
	if err != nil {
		log.Fatal(err)
	}

	err = os.Remove("./" + filename + ".gz")
	if err != nil {
		log.Fatal(err)
	}
}
