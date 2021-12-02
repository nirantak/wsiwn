package main

import (
	"github.com/nirantak/wsiwn/cli"
	"github.com/spf13/viper"
)

const Version string = "2.0.1"

func init() {
	viper.Set("version", Version)
}

func main() {
	cli.Execute()
}
