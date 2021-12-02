package cli

import (
	"fmt"
	"os"

	"github.com/spf13/viper"
)

func log(verbose bool, msg ...interface{}) {
	if verbose && !viper.GetBool("verbose") {
	} else {
		fmt.Fprintln(os.Stderr, msg...)
	}
}
