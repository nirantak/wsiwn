package cli

import (
	"fmt"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

const cfgFile string = "wsiwn_config.yml"

var Verbose bool

var rootCmd = &cobra.Command{
	Use:   "wsiwn",
	Short: "What Should I Watch Next?",
	Long: `WSIWN (What Should I Watch Next?) is a CLI tool to help you decide what to watch next.
You can use it to filter though movies and TV shows in the IMDb database using various search criteria.`,
}

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "WSIWN CLI Version",
	Long:  `Version of the WSIWN CLI tool installed`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Printf("WSIWN v%s\n", viper.GetString("version"))
	},
}

func Execute() {
	cobra.CheckErr(rootCmd.Execute())
}

func init() {
	cobra.OnInitialize(initConfig)

	rootCmd.PersistentFlags().BoolVarP(&Verbose, "verbose", "v", false, "verbose output")
	rootCmd.AddCommand(versionCmd)
	viper.BindPFlag("verbose", rootCmd.PersistentFlags().Lookup("verbose"))
}

func initConfig() {
	viper.SetConfigFile(cfgFile)
	viper.SetEnvPrefix("wsiwn")
	viper.AutomaticEnv()

	if err := viper.ReadInConfig(); err == nil {
		log(true, "Using config file:", viper.ConfigFileUsed())
	} else {
		log(true, "No config file found, using default values")
	}
}
