package api

import "github.com/spf13/viper"

const Version string = "2.0.1"

func init() {
	viper.Set("version", Version)
}
