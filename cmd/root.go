package cmd

import (
	"github.com/spf13/cobra"
)

const Version string = "2.0.1"

var Verbose bool

var rootCmd = &cobra.Command{
	Use:     "wsiwn",
	Version: Version,
	Short:   "What Should I Watch Next?",
	Long: `WSIWN (What Should I Watch Next?) is a CLI tool to help you decide what to watch next.
You can use it to filter though movies and TV shows in the IMDb database using various search criteria.`,
}

func Execute() {
	cobra.CheckErr(rootCmd.Execute())
}

func init() {
	rootCmd.PersistentFlags().BoolVarP(&Verbose, "verbose", "V", false, "verbose output")
}
